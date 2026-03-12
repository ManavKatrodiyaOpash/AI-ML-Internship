import streamlit as st
import pickle
import numpy as np
import difflib

# ======================
# Load Model Files
# ======================
with open("book_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("pivot.pkl", "rb") as f:
    pivot_table = pickle.load(f)

book_list = list(pivot_table.index)

# ======================
# Page Config
# ======================
st.set_page_config(page_title="Book Recommendation System", layout="centered")

st.title("📚 Book Recommendation System")
st.write("Search a book or type your own name")

# ======================
# Single Smart Input
# ======================
book_name = st.selectbox(
    "Search or type a book",
    options=book_list,
    index=None,
    placeholder="Start typing a book name...",
    accept_new_options=True
)

# ======================
# Recommendation Function
# ======================
def recommend_book(book_name):

    # make user input lowercase
    search = book_name.strip().lower()

    # convert dataset titles to lowercase for comparison
    titles_lower = [title.lower() for title in book_list]

    # check if exact title exists ignoring case
    if search not in titles_lower:
        return None

    # get the correct original title
    index = titles_lower.index(search)
    book = book_list[index]

    book_id = np.where(pivot_table.index == book)[0][0]

    distances, suggestions = model.kneighbors(
        pivot_table.iloc[book_id, :].values.reshape(1, -1),
        n_neighbors=6
    )

    rec_books = []

    for i in suggestions[0]:
        rec_books.append(pivot_table.index[i])

    return rec_books[1:], book


# ======================
# Button
# ======================
if st.button("Recommend Books"):

    if not book_name:
        st.warning("Please enter a book name")

    else:
        result = recommend_book(book_name)

        if result is None:
            st.error("❌ Book not found in database")

        else:
            recommendations, matched_book = result

            st.success(f"Showing results for: **{matched_book}**")

            for book in recommendations:
                st.write("📖", book)