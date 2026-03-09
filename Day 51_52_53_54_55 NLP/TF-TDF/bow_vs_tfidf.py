documents = [
"AI is the future",
"I love learning AI",
"AI will change the world",
"Machine learning is powerful",
"I enjoy studying machine learning",
"AI and machine learning are amazing",
"Deep learning drives modern AI",
"AI is transforming technology"
]

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Bag of Words
bow_vectorizer = CountVectorizer()
bow_matrix = bow_vectorizer.fit_transform(documents)
print("Bag of Words Matrix:")
print(bow_matrix.toarray())
print("\nFeature Names (Bag of Words):")
print(bow_vectorizer.get_feature_names_out())

# TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())
print("\nFeature Names (TF-IDF):")
print(tfidf_vectorizer.get_feature_names_out())