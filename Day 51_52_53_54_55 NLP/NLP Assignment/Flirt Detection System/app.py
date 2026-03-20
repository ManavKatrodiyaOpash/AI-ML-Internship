
# import streamlit as st
# import joblib
# import pandas as pd

# # Load the saved model and vectorizer
# @st.cache_resource
# def load_resources():
#     model = joblib.load('logistic_regression_model.pkl')
#     vectorizer = joblib.load('tfidf_vectorizer.pkl')
#     return model, vectorizer

# model, vectorizer = load_resources()

# st.title('Flirt Detection App')
# st.write("Enter a message below to detect if it's flirtatious or not.")

# user_input = st.text_area('Enter your message here:')

# if st.button('Detect Flirt'):
#     if user_input:
#         # Preprocess the input text
#         processed_input = user_input.lower() # Based on our preprocessing steps
#         # Tokenization and punctuation removal would typically happen here if not already done by the vectorizer
        
#         # Transform the input using the loaded TF-IDF vectorizer
#         input_vectorized = vectorizer.transform([processed_input])
        
#         # Make prediction
#         prediction = model.predict(input_vectorized)
        
#         if prediction[0] == 1:
#             st.success('Prediction: This message is likely **Flirtatious**! 😉')
#         else:
#             st.info('Prediction: This message is likely **Not Flirtatious**. 😊')
#     else:
#         st.warning('Please enter a message to detect.')














import streamlit as st
import joblib
import pandas as pd

# Load the saved model and vectorizer
@st.cache_resource
def load_resources():
    # Adding error handling in case files are missing
    try:
        model = joblib.load('logistic_regression_model.pkl')
        vectorizer = joblib.load('tfidf_vectorizer.pkl')
        return model, vectorizer
    except Exception as e:
        st.error(f"Error loading model files: {e}")
        return None, None

model, vectorizer = load_resources()

st.title('Flirt Detection App')
st.write("Enter a message below to detect if it's flirtatious or not.")

user_input = st.text_area('Enter your message here:', height=150)

if st.button('Detect Flirt'):
    if user_input.strip() and model is not None:
        # Preprocess and Transform
        input_vectorized = vectorizer.transform([user_input])
        
        # Make prediction
        prediction = model.predict(input_vectorized)
        
        # Get probabilities for [Class 0, Class 1]
        probabilities = model.predict_proba(input_vectorized)[0]
        confidence = max(probabilities) * 100  # Get the highest probability as %
        
        
        # st.write(probabilities)  # Debug: Show raw probabilities
        # st.write(prediction)

        if prediction[0] == 1:
            st.success(f'Prediction: **Flirtatious** 😉')
            st.write(f"**Confidence:** {confidence:.2f}%")
            st.progress(confidence / 100)
        else:
            st.info(f'Prediction: **Not Flirtatious** 😊')
            st.write(f"**Confidence:** {confidence:.2f}%")
            st.progress(confidence / 100)
        
    else:
        st.warning('Please enter a message to detect.')