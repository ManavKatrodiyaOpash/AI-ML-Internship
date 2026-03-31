import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate


PDF_PATH = "books/A Game Of Thrones - George R. R. Martin.pdf"
DB_PATH = "faiss_index"


# 🔹 LOAD + SPLIT (optimized for long docs)
def load_and_split():
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,      # smaller = better precision
        chunk_overlap=250
    )
    return splitter.split_documents(docs)


# 🔹 CREATE DB
def create_db():
    docs = load_and_split()

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-large-en",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
)

    db = FAISS.from_documents(docs, embeddings)
    db.save_local(DB_PATH)
    print("✅ Vector DB Created!")


# 🔹 LOAD DB
def load_db():
    if not os.path.exists(DB_PATH):
        raise Exception("Run create_db() first!")

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    return FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )


# 🔹 RAG CHAIN
def get_chain():
    db = load_db()

    # ✅ Better retrieval for large docs
    retriever = db.as_retriever(
        search_type="similarity",  
        search_kwargs={"k": 10}
    )

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        temperature=0.3
    )

    prompt = ChatPromptTemplate.from_template("""
        You are a Game of Thrones expert assistant.

        Use ONLY the given context.
        Also use previous conversation if needed.

        If answer is not found, say: "Not found in book".

        Conversation History:
        {history}

        Context:
        {context}

        Question:
        {question}

        Answer in detailed but clear way.
        """)

    return retriever, llm, prompt

from sentence_transformers import CrossEncoder

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, docs):
    pairs = [(query, d.page_content) for d in docs]
    scores = reranker.predict(pairs)

    ranked = sorted(zip(scores, docs), reverse=True, key=lambda x: x[0])
    return [doc for _, doc in ranked[:5]]

# 🔹 ASK FUNCTION (clean + correct)
def ask(query, chat_history=None):
    retriever, llm, prompt = get_chain()

    docs = retriever.invoke(query)

    # 🔥 RERANK
    docs = rerank(query, docs)

    context = "\n\n".join([d.page_content for d in docs])

    history_text = ""
    if chat_history:
        history_text = "\n".join(
            [f"{m['role']}: {m['content']}" for m in chat_history[-5:]]
        )

    chain = prompt | llm

    answer = chain.invoke({
        "context": context,
        "question": query,
        "history": history_text
    })

    return answer.content, docs
      


# 🔹 MAIN
if __name__ == "__main__":
    # Run once
    # create_db()

    ans, src = ask("What happens in prologue?")

    print("\nANSWER:\n", ans)

    print("\nSOURCES:")
    for s in src:
        print(f"Page: {s['page']}")
        print(s['text'])
        print("------")