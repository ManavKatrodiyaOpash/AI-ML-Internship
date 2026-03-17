import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from transformers import pipeline

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Emotion Detection NLP",
    page_icon="😊",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("😊 NLP Emotion Detection System")
st.markdown(
"""
This application detects **human emotions from text** using a pretrained **Transformer model**.

Model used:
`j-hartmann/emotion-english-distilroberta-base`
"""
)

st.divider()

# -----------------------------------
# LOAD MODEL
# -----------------------------------

@st.cache_resource
def load_model():
    emotion_model = pipeline(
        "sentiment-analysis",
        model="j-hartmann/emotion-english-distilroberta-base"
    )
    return emotion_model

emotion = load_model()

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.header("Options")

mode = st.sidebar.radio(
    "Choose Mode",
    ["Single Text Prediction", "Dataset Analysis"]
)

# -----------------------------------
# SINGLE TEXT PREDICTION
# -----------------------------------

if mode == "Single Text Prediction":

    st.subheader("Enter Text")

    user_input = st.text_area(
        "Write something:",
        "I am feeling very happy today!"
    )

    if st.button("Analyze Emotion"):

        result = emotion(user_input)[0]

        label = result["label"]
        score = result["score"]

        st.success(f"Detected Emotion: **{label}**")
        st.metric("Confidence", f"{score*100:.2f}%")

# -----------------------------------
# DATASET ANALYSIS
# -----------------------------------

elif mode == "Dataset Analysis":

    st.subheader("Upload Dataset")

    uploaded_file = st.file_uploader(
        "Upload CSV file",
        type=["csv"]
    )

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

        st.write("Dataset Preview")

        st.dataframe(df.head())

        if "content" not in df.columns:

            st.error("Dataset must contain a column named 'content'")
            st.stop()

        sample_size = st.slider(
            "Number of rows to analyze",
            50,
            min(1000, len(df)),
            200
        )

        df = df.sample(sample_size)

        st.info("Running emotion detection...")

        def get_emotion(text):
            return emotion(text)[0]["label"]

        df["emotion"] = df["content"].apply(get_emotion)

        st.write("Prediction Results")

        st.dataframe(df)

        # ----------------------------
        # EMOTION DISTRIBUTION
        # ----------------------------

        st.subheader("Emotion Distribution")

        fig, ax = plt.subplots()

        sns.countplot(
            y="emotion",
            data=df,
            order=df["emotion"].value_counts().index,
            ax=ax
        )

        plt.title("Emotion Detection")

        st.pyplot(fig)