from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I love machine learning",
    "Machine learning is amazing",
    "I love deep learning"
]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

print(tfidf_matrix.toarray())