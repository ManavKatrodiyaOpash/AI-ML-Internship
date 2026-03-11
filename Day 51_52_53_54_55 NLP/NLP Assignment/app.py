import streamlit as st
import pickle
import string

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

stop_words = stopwords.words("english")
ps = PorterStemmer()

def transform_text(text):
    # Lowercase
    text = text.lower()

    # Tokenization
    text = nltk.word_tokenize(text)

    # Removing Special Punctuation
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    # Removing stop words and punctuation
    text = y[:]
    y.clear()

    for i in text:
        if i not in stop_words and i not in string.punctuation:
            y.append(i)
    
    # Stemming
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter your message")

if st.button("Predict"):

    # 1. Preprocess
    transformed_sms = transform_text(input_sms)

    # 2. Vectorize
    vector = tfidf.transform([transformed_sms])

    # 3. Predict
    result = model.predict(vector)[0]

    # 4. Display result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

# example text = "you could be entitled up to $3,160 in compensation from  mis-sold PPI on a credit card or loan. Please  reply PPI for info or stop to opt out"

# example text = "SIX chances to win CASH! From 100 to 20,000 pounds txt> CSH11 and send to 87575. Cost 150p/day, 6days, 16+ TsandCs apply Reply HL 4 info"

# example text = "Hey i saw you presentation today it was good"

# example text = "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's"