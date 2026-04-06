import os
import glob
from dotenv import load_dotenv

load_dotenv()

import torch
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from sentence_transformers import CrossEncoder


BOOKS_DIR = "books"
DB_PATH   = "faiss_index"

# ─────────────────────────────────────────────
# ⚡ AUTO DEVICE DETECTION — GPU if available, else CPU
# ─────────────────────────────────────────────
if torch.cuda.is_available():
    DEVICE = "cuda"
    gpu_name = torch.cuda.get_device_name(0)
    print(f"⚡ GPU detected: {gpu_name} — running on CUDA")
else:
    DEVICE = "cpu"
    print("💻 No GPU detected — running on CPU")

# ─────────────────────────────────────────────
# 🔹 LOAD ALL PDFs from books/ folder
# ─────────────────────────────────────────────
def load_and_split():
    pdf_files = sorted(glob.glob(os.path.join(BOOKS_DIR, "*.pdf")))

    if not pdf_files:
        raise FileNotFoundError(
            f"No PDF files found in '{BOOKS_DIR}/' folder.\n"
            "Please place all 5 ASOIAF books as PDFs inside the books/ folder."
        )

    print(f"📚 Found {len(pdf_files)} book(s):")
    for f in pdf_files:
        print(f"   → {os.path.basename(f)}")

    all_docs = []
    for pdf_path in pdf_files:
        book_name = os.path.splitext(os.path.basename(pdf_path))[0]
        print(f"   Loading: {book_name} ...")
        loader = PyPDFLoader(pdf_path)
        docs   = loader.load()

        # Tag every chunk with its source book
        for doc in docs:
            doc.metadata["book"] = book_name

        all_docs.extend(docs)

    print(f"✅ Total pages loaded: {len(all_docs)}")

    # ── Smarter splitting ──────────────────────────────────────
    # Larger chunks → more context per retrieval → fewer "lost" answers
    # Higher overlap → appendix / house-detail passages stay intact
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=400,
        separators=["\n\n", "\n", ".", " ", ""]   # respect paragraph boundaries
    )

    chunks = splitter.split_documents(all_docs)
    print(f"✅ Total chunks created: {len(chunks)}")
    return chunks


# ─────────────────────────────────────────────
# 🔹 CREATE VECTOR DB  (run once per book set)
# ─────────────────────────────────────────────
def create_db():
    chunks = load_and_split()

    # bge-large gives the best retrieval quality for long fiction
    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-large-en",
        model_kwargs={"device": DEVICE},          # ⚡ auto GPU / CPU
        encode_kwargs={"normalize_embeddings": True}
    )

    print(f"⚙️  Building FAISS index on {DEVICE.upper()} (this may take a few minutes)...")
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(DB_PATH)
    print("✅ Vector DB saved!")


# ─────────────────────────────────────────────
# 🔹 LOAD VECTOR DB
# ─────────────────────────────────────────────
def load_db():
    if not os.path.exists(DB_PATH):
        raise Exception(
            "Vector DB not found!\n"
            "Run  python rag.py  once to build the index from your PDFs."
        )

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-large-en",          # ← same model used at index time
        model_kwargs={"device": DEVICE},          # ⚡ auto GPU / CPU
        encode_kwargs={"normalize_embeddings": True}
    )

    return FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )


# ─────────────────────────────────────────────
# 🔹 RERANKER  (CrossEncoder for precision)
# ─────────────────────────────────────────────
reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2",
    device=DEVICE                                 # ⚡ auto GPU / CPU
)

def rerank(query, docs, top_k=6):
    pairs  = [(query, d.page_content) for d in docs]
    scores = reranker.predict(pairs)
    ranked = sorted(zip(scores, docs), reverse=True, key=lambda x: x[0])
    return [doc for _, doc in ranked[:top_k]]


# ─────────────────────────────────────────────
# 🔹 BUILD RAG CHAIN
# ─────────────────────────────────────────────
def get_chain():
    db = load_db()

    # Retrieve more candidates before reranking
    retriever = db.as_retriever(
        search_type="mmr",                        # MMR reduces duplicate chunks
        search_kwargs={"k": 15, "fetch_k": 30}
    )

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2                           # lower = more factual
    )

    # Improved prompt: instructs the model to use appendix / lore details
    prompt = ChatPromptTemplate.from_template("""
You are an expert on the "A Song of Ice and Fire" book series by George R. R. Martin.
You have deep knowledge of all five books:
  1. A Game of Thrones
  2. A Clash of Kings
  3. A Storm of Swords
  4. A Feast for Crows
  5. A Dance with Dragons

RULES:
- Answer ONLY from the Context provided below.
- The Context includes chapters, appendices, and house/character details — use ALL of it.
- If the answer spans multiple books, mention which book it comes from.
- If a detail is in the appendix (houses, sigils, words, members), include it in your answer.
- If the answer is truly not in the context, say exactly: "Not found in the books."
- Do NOT invent facts. Do NOT use outside knowledge.
- Be detailed, clear, and well-structured.

Conversation History (last 5 turns):
{history}

Context from the books:
{context}

Question: {question}

Answer:
""")

    return retriever, llm, prompt


# ─────────────────────────────────────────────
# 🔹 ASK  (main entry point)
# ─────────────────────────────────────────────
def ask(query, chat_history=None):
    retriever, llm, prompt = get_chain()

    # Step 1 – retrieve candidates
    docs = retriever.invoke(query)

    # Step 2 – rerank for precision
    docs = rerank(query, docs, top_k=6)

    # Step 3 – build context with book labels
    context_parts = []
    for doc in docs:
        book  = doc.metadata.get("book", "Unknown Book")
        page  = doc.metadata.get("page", "?")
        context_parts.append(f"[{book} | Page {page}]\n{doc.page_content}")
    context = "\n\n---\n\n".join(context_parts)

    # Step 4 – build history string
    history_text = ""
    if chat_history:
        history_text = "\n".join(
            [f"{m['role'].capitalize()}: {m['content']}" for m in chat_history[-6:]]
        )

    # Step 5 – invoke LLM
    chain  = prompt | llm
    answer = chain.invoke({
        "context":  context,
        "question": query,
        "history":  history_text
    })

    return answer.content, docs


# ─────────────────────────────────────────────
# 🔹 MAIN  – build DB when run directly
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  ASOIAF Vector DB Builder")
    print("=" * 55)
    print("\nBuilding vector database from all books in books/ ...\n")
    create_db()
    print("\n✅ Done! You can now run:  streamlit run app.py\n")
