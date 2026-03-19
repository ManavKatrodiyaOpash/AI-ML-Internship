import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# ===============================
# LOAD MODEL
# ===============================
model_path = "flirt_detection_model"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

classifier = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer
)

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Flirt Detection AI",
    page_icon="💕",
    layout="centered"
)

# ===============================
# UI
# ===============================
st.markdown(
    "<h1 style='text-align:center;'>💕 Flirt Detection AI</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Analyze messages using AI to detect flirting</p>",
    unsafe_allow_html=True
)

st.divider()

# ===============================
# INPUT
# ===============================
text = st.text_area(
    "Enter your message",
    height=150,
    placeholder="Example: You look amazing today..."
)

# ===============================
# BUTTON
# ===============================
if st.button("Analyze Message"):

    if text.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:

        with st.spinner("Analyzing..."):

            result = classifier(text)[0]

            label = result["label"]
            score = result["score"]

            if label == "LABEL_1":
                prob_flirt = score
            else:
                prob_flirt = 1 - score

        st.divider()

        # RESULT
        st.subheader("Result")

        st.metric(
            "Flirt Probability",
            f"{prob_flirt*100:.2f}%"
        )

        # VISUAL FEEDBACK
        if prob_flirt > 0.75:
            st.success("💖 Strong Flirting Detected")
        elif prob_flirt > 0.45:
            st.info("😉 Mild / Possible Flirting")
        else:
            st.info("😐 Not Flirting")

# ===============================
# FOOTER
# ===============================
st.divider()
st.caption("Built with ❤️ using DistilBERT + Streamlit")