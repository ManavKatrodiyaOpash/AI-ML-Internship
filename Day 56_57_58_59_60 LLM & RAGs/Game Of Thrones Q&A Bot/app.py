import streamlit as st
from rag import ask

# ─────────────────────────────────────────────
# Page config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="A Song Of Ice And Fire Chatbot",
    page_icon="🐉",
    layout="centered"
)

# ─────────────────────────────────────────────
# Custom CSS — footer + chat styling
# ─────────────────────────────────────────────
st.markdown("""
<style>
    /* Footer fixed at bottom */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #0e1117;
        border-top: 1px solid #2e2e2e;
        padding: 8px 0;
        text-align: center;
        font-size: 13px;
        color: #888;
        z-index: 9999;
    }
    .footer span {
        color: #c0392b;
        font-weight: 600;
    }

    /* Add bottom padding so chat isn't hidden behind footer */
    .main .block-container {
        padding-bottom: 80px;
    }
</style>

<div class="footer">
    ⚔️ Game Of Thrones AI Chatbot &nbsp;|&nbsp; Made with ❤️ by <span>Manav Katrodiya</span>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────
st.title("🐉 Game Of Thrones AI Chatbot")
st.caption("Ask anything across all 5 books of Song Of Ice And Fire — characters, houses, events, lore & more!")

# Book list info
with st.expander("📚 Books loaded in this chatbot"):
    st.markdown("""
    1. **A Game of Thrones** (Book 1)
    2. **A Clash of Kings** (Book 2)
    3. **A Storm of Swords** (Book 3)
    4. **A Feast for Crows** (Book 4)
    5. **A Dance with Dragons** (Book 5)

    > Includes chapters, appendices, house details, sigils, words & character lists.
    """)

st.divider()

# ─────────────────────────────────────────────
# Session memory
# ─────────────────────────────────────────────
if "chat" not in st.session_state:
    st.session_state.chat = []

# Clear chat button
# col1, col2 = st.columns([8, 2])
# with col2:
#     if st.button("🗑️ Clear Chat"):
#         st.session_state.chat = []
#         st.rerun()

# ─────────────────────────────────────────────
# Display chat history
# ─────────────────────────────────────────────
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ─────────────────────────────────────────────
# Input
# ─────────────────────────────────────────────
query = st.chat_input("Ask about Westeros, Essos, houses, characters, events...")

if query:
    # Save & show user message
    st.session_state.chat.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    # Get & show assistant answer
    with st.chat_message("assistant"):
        with st.spinner("Searching the books... 📖"):
            answer, sources = ask(query, st.session_state.chat)
            st.write(answer)

            # Show source books used (collapsed by default)
            if sources:
                books_used = sorted(set(
                    s.metadata.get("book", "Unknown") for s in sources
                ))
                with st.expander("📖 Sources used"):
                    for b in books_used:
                        st.markdown(f"- {b}")

    # Save assistant response
    st.session_state.chat.append({"role": "assistant", "content": answer})
