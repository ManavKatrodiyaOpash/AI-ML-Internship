# 🐉 A Song of Ice and Fire — AI Chatbot
**Made by Manav Katrodiya**

---

## 📚 Setup Instructions

> ⚠️ Use Python 3.11 It is more stable and faster than current versions.

### Step 1 — Add your books
Make and Place all 5 A Song Of Ice And Fire PDFs inside the `books/` folder:
```
books/
  A Game of Thrones.pdf
  A Clash of Kings.pdf
  A Storm of Swords.pdf
  A Feast for Crows.pdf
  A Dance with Dragons.pdf
```
> The filenames don't have to match exactly — any `.pdf` files in the folder will be loaded.

---

### Step 2 — Add your API key
Edit `.env` and paste your key (Any API key will work):
```
{Company_Name}_API_KEY=your_API_key_here
```
Example :-
```
GEMINI_API_KEY=your_GEMINI_API_key_here
OPENAI_API_KEY=your_OPENAI_API_key_here
```
---

### Step 3 — Install dependencies
```bash
pip install -r requirement.txt
```

---

### Step 4 — Build the Vector Database (ONE TIME ONLY)
```bash
python rag.py
```
⚠️ This reads all PDFs and builds the FAISS index. It takes a few minutes depends upon the system you are using.
You only need to do this **once**. If you add new books later, run it again.

---

### Step 5 — Run the chatbot
```bash
streamlit run app.py
```

---

## 💡 What's improved in this version

| Feature | Old Version | New Version |
|---|---|---|
| Books | 1 (GOT only) | All 5 A Song Of Ice And Fire Books |
| Chunk size | 1200 | 1500 (more context) |
| Chunk overlap | 250 | 400 (appendix-safe) |
| Retrieval | similarity k=10 | MMR k=15 (no duplicates) |
| Reranker top_k | 5 | 6 |
| Embedding model | all-MiniLM-L6-v2 (load) vs bge-large (index) | bge-large-en for BOTH |
| Prompt | Basic | Appendix-aware, book-labeled |
| Source display | None | Shows which book answered |
| Clear chat | None | ✅ Button added |