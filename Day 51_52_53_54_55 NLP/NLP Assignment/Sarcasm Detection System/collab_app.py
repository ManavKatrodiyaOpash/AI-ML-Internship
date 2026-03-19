import streamlit as st
from transformers import pipeline
import torch

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Sarcasm Detector",
    page_icon="😂",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ================== CUSTOM CSS ==================
st.markdown("""
<style>
    .big-font {font-size: 60px !important; text-align: center;}
    .result-box {padding: 20px; border-radius: 15px; text-align: center; margin: 20px 0;}
    .sarcastic {background: linear-gradient(90deg, #ff4d4d, #ff9999); color: white;}
    .normal {background: linear-gradient(90deg, #4CAF50, #8BC34A); color: white;}
</style>
""", unsafe_allow_html=True)

# ================== TITLE ==================
st.title("😂 Sarcasm Detection")

# ================== MODEL LOADING (cached) ==================
@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="sarcasm_model_collab",                    # ← put your model folder here
        device=0 if torch.cuda.is_available() else -1
    )

classifier = load_model()

# ================== INPUT ==================
headline = st.text_area(
    "Write a text here 👇",
    height=120
)

# ================== DETECT BUTTON ==================
if st.button("🔍 Check for Sarcasm", type="primary", use_container_width=True):
    if headline.strip():
        with st.spinner("Analyzing headline..."):
            result = classifier(headline)[0]
            
            label = result["label"]
            score = result["score"]
            
            # LABEL_1 = sarcastic (because we trained 1 = sarcastic)
            if label == "LABEL_1":
                st.markdown(f"""
                <div class='result-box sarcastic'>
                    <h2>😂 SARCASTIC!</h2>
                    <h3>Confidence: {score:.1%}</h3>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
            else:
                st.markdown(f"""
                <div class='result-box normal'>
                    <h2>🙂 NOT SARCASTIC</h2>
                    <h3>Confidence: {score:.1%}</h3>
                </div>
                """, unsafe_allow_html=True)
                
            # Progress bar
            st.progress(score)
            
    else:
        st.warning("Please enter a headline first!")