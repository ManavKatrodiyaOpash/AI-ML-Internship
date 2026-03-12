import streamlit as st
import pickle
import numpy as np

# ======================
# Load Model Files
# ======================
movies = pickle.load(open("movies.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

movie_list = movies["title"].values

# ======================
# Page Config
# ======================
st.set_page_config(page_title="Movie Recommendation System", layout="centered")

st.title("🎬 Movie Recommendation System")
st.write("Search a movie or type your own name")

# ======================
# Single Smart Input
# ======================
movie_name = st.selectbox(
    "Search or type a movie",
    options=movie_list,
    index=None,
    placeholder="Start typing a movie...",
    accept_new_options=True
)

# ======================
# Recommendation Function
# ======================
def recommend(movie):

    search = movie.strip().lower()
    titles_lower = [title.lower() for title in movie_list]

    if search not in titles_lower:
        return None

    index = titles_lower.index(search)
    movie_index = movies.iloc[index].name

    distances = similarity[movie_index]

    movie_list_sorted = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x:x[1]
    )[1:6]

    rec_movies = []

    for i in movie_list_sorted:
        rec_movies.append(movies.iloc[i[0]].title)

    return rec_movies

# ======================
# Button
# ======================
if st.button("Recommend Movies"):

    if not movie_name:
        st.warning("Please enter a movie name")

    else:
        result = recommend(movie_name)

        if result is None:
            st.error("❌ Movie not found in database")

        else:
            st.success("Recommended Movies")

            for m in result:
                st.write("🎬", m)