from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

df = pd.read_csv("data.csv")

documents = [
    "I love machine learning",
    "Machine learning is amazing",
    "I love deep learning"
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)
tfidf_matrix_2 = vectorizer.fit_transform(df["text"])

print(tfidf_matrix.toarray())
print()
print(tfidf_matrix_2.toarray())