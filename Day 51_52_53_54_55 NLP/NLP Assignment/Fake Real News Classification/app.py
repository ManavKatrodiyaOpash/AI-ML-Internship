import streamlit as st
import numpy as np
import spacy
import pickle

# ------------------------------
# PAGE CONFIG
# ------------------------------

st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="wide"
)

st.title("📰 Fake News Detection System")

st.markdown("""
This system detects whether a news article is **REAL or FAKE**.

The model is trained on a dataset of news articles and uses natural language processing techniques to analyze the text and make predictions.
""")

st.divider()

# ------------------------------
# LOAD MODEL
# ------------------------------

@st.cache_resource
def load_model():

    model = pickle.load(open("fake_news_model.pkl", "rb"))

    nlp = spacy.load("en_core_web_lg")

    return model, nlp

model, nlp = load_model()

# ------------------------------
# PREPROCESS FUNCTION
# ------------------------------

def preprocess_and_vectorize(text):

    doc = nlp(text)

    filtered_vectors = []

    for token in doc:

        if token.is_stop or token.is_punct:
            continue

        if token.has_vector:
            filtered_vectors.append(token.vector)

    if not filtered_vectors:
        return np.zeros((300,))

    return np.mean(filtered_vectors, axis=0)

# ------------------------------
# INPUT AREA
# ------------------------------

news_text = st.text_area(
    "Enter News Article"
)

# ------------------------------
# PREDICTION
# ------------------------------

if st.button("Detect News"):
    
    if news_text.strip() == "":
        st.warning("Please enter a news article.")
    
    else:

        vector = preprocess_and_vectorize(news_text)

        prediction = model.predict([vector])[0]

        if prediction == 1:

            st.success("🟢 This news is REAL")

        else:

            st.error("🔴 This news is FAKE")