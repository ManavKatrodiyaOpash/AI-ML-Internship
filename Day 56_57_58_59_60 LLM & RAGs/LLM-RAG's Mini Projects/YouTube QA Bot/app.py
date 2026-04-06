import streamlit as st
from dotenv import load_dotenv

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

# ---------------- CONFIG ----------------
load_dotenv()

st.set_page_config(
    page_title="YouTube AI Chatbot",
    page_icon="🎥",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.chat-container {
    border-radius: 15px;
    padding: 15px;
}
.stChatMessage {
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🎥 YouTube Video AI Chatbot")
st.caption("Chat with any YouTube video using AI ⚡")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ Settings")
    
    language = ["English", "Hindi", "Gujarati"]

    video_id = st.text_input("Enter YouTube Video ID")
    video_lang_id = st.selectbox("Select Language of the YouTube Video", language, index=0)

    process_btn = st.button("🚀 Process Video")

    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.markdown("""
    - Use videos with captions
    - Use Only the Video ID (e.g. `dQw4w9WgXcQ`) not the full URL
    - Also supports Hindi and Gujarati videos with captions
    - The first time processing may take a while, grab a coffee ☕
    """)

# ---------------- SESSION STATE ----------------
if "chain" not in st.session_state:
    st.session_state.chain = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- CACHE FUNCTION ----------------
@st.cache_resource
def process_video(video_id):
    
    lang_dict = {
        "English": "en",
        "Hindi": "hi",
        "Gujarati": "gu"
    }
    
    api = YouTubeTranscriptApi()
    transcript_list = api.fetch(video_id, languages=[lang_dict.get(video_lang_id)])
    transcript = " ".join(chunk.text for chunk in transcript_list)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=100
    )
    chunks = splitter.create_documents([transcript])

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(chunks, embeddings)

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.2
    )

    prompt = PromptTemplate(
        template="""
        You are a helpful youtube video ai assistant.
        Answer ONLY from the transcript.
        If not found, say "I don't know".
        
        Rules :-
        - NEVER answer from your own knowledge, only use the transcript
        - Use your best judgement to answer from the transcript, don't just copy paste
        - If the answer is not found in the transcript, say "I don't know"
        - Always answer the question using the language of the question, even if the transcript is in a different language

        Context: {context}
        Question: {question}
        """,
        input_variables=["context", "question"]
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    parallel_chain = RunnableParallel({
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    })

    main_chain = parallel_chain | prompt | llm | StrOutputParser()

    return main_chain

# ---------------- PROCESS VIDEO ----------------
if process_btn and video_id:
    try:
        with st.spinner("⏳ Processing video..."):
            st.session_state.chain = process_video(video_id)
            st.session_state.chat_history = []

        st.success("✅ Video ready! Start chatting below.")

    except TranscriptsDisabled:
        st.error("❌ No captions available")
    except Exception as e:
        st.error(f"Error: {e}")

# ---------------- CHAT UI ----------------

if st.session_state.chain:

    user_input = st.chat_input("Ask something about the video...")

    if user_input:
        response = st.session_state.chain.invoke(user_input)

        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("bot", response))

    # Display messages
    for role, msg in st.session_state.chat_history:
        if role == "user":
            with st.chat_message("user"):
                st.markdown(msg)
        else:
            with st.chat_message("assistant"):
                st.markdown(msg)

else:
    st.markdown("## 💬 Chat")
    st.info("👈 Enter a YouTube Video ID and language transcript of the YouTube Video in the sidebar and click 'Process Video'")