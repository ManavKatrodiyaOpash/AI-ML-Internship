import streamlit as st
import joblib

# Load model
model = joblib.load('sarcasm_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.set_page_config(page_title="Sarcasm Detection", page_icon="😏")
st.title("📰 Sarcasm Detection System")
st.markdown("### Enter any text here and I'll tell you if it's sarcastic")

headline = st.text_area("Write text here:", height=150)

if st.button("Detect Sarcasm", type="primary"):
    if headline.strip() == "":
        st.warning("Please enter a headline")
    else:
        # Predict
        vec = vectorizer.transform([headline])
        prediction = model.predict(vec)[0]
        prob = model.predict_proba(vec)[0]

        if prediction == 1:
            st.success("😏 **SARCASTIC**")
            st.metric("Confidence", f"{prob[1]*100:.1f}%")
            st.balloons()
        else:
            st.info("😐 **NOT SARCASTIC**")
            st.metric("Confidence", f"{prob[0]*100:.1f}%")