import pandas as pd
import random

positive_reviews = [
    "This movie was amazing and the acting was fantastic",
    "I really loved this film it was wonderful",
    "Great storyline and brilliant performances",
    "One of the best movies I have ever watched",
    "Absolutely loved the cinematography and direction",
    "The characters were very engaging and emotional",
    "Fantastic movie with a beautiful story",
    "A masterpiece with great acting and music",
    "Highly recommended movie for everyone",
    "This film was truly inspiring and enjoyable"
]

negative_reviews = [
    "This movie was terrible and boring",
    "I hated this film it was very disappointing",
    "Worst movie I have ever watched",
    "The storyline was weak and acting was bad",
    "Very slow and uninteresting film",
    "Completely waste of time",
    "The movie had poor direction and editing",
    "Awful movie with no good scenes",
    "Terrible acting and bad screenplay",
    "I regret watching this movie"
]

reviews = []
labels = []

for i in range(5000):
    reviews.append(random.choice(positive_reviews))
    labels.append(1)

for i in range(5000):
    reviews.append(random.choice(negative_reviews))
    labels.append(0)

data = pd.DataFrame({
    "review": reviews,
    "label": labels
})

data = data.sample(frac=1).reset_index(drop=True)

data.to_csv("movie_reviews_dataset.csv", index=False)

print("Dataset created successfully")