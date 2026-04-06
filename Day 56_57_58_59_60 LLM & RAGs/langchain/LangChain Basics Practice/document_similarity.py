from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

documnents = [
    "Virat Kohli is the captain of the Indian cricket team.",
    "Sachin Tendulkar is a former Indian cricketer.",
    "MS Dhoni is a former captain of the Indian cricket team.",
    "Jasprit Bumrah is a fast bowler in the Indian cricket team."
]

query = "tell me about virat kohli"

doc_emdeddings = embeddings.embed_documents(documnents)
query_embedding = embeddings.embed_query(query)

scores = cosine_similarity([query_embedding], doc_emdeddings)

index, score = sorted(list(enumerate(scores)), key = lambda x: x[1])[-1]

print(query)
print(documnents[index])
print("Similarity Score :-", score)