import streamlit as st
from rag import ask

st.set_page_config(page_title="GOT Chatbot", page_icon="🐉")

st.title("🐉 Game of Thrones AI Chatbot")
st.caption("Ask anything from the book")

# 🔹 Session memory
if "chat" not in st.session_state:
    st.session_state.chat = []

# 🔹 Display chat
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 🔹 Input
query = st.chat_input("Ask about Westeros...")

if query:
    # Save user message
    st.session_state.chat.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🧠"):
            answer, _ = ask(query, st.session_state.chat)
            st.write(answer)

    # Save assistant response
    st.session_state.chat.append({"role": "assistant", "content": answer})