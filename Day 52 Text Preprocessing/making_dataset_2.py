import pandas as pd
import random

names = [
    "Dark City", "Future War", "Love Story", "Galaxy Mission",
    "Silent Hill", "Night Hunter", "Final Kingdom", "Ocean Fear"
]

genres = ["Action","Drama","Comedy","Sci-Fi","Horror","Adventure"]

messy_descriptions = [
    "OMG this movie is soooo good!!! 😍😍 <br> visit http://movie.com",
    "I luv this film sooo much lol!!! 😂😂",
    "Worst movie ever!!! don't watch it bro 😡😡 www.badmovie.com",
    "<p>This movie was amazng!!! must watch!!!</p>",
    "gr8 acting and storyline... totally worth it!!! 😎",
    "idk why ppl hate this movie lol it's awesome!!!",
    "sooo boring movie... waste of time!!! 😴",
    "best film everrrrr!!! check https://filmreview.com",
    "terrible acting omg!!! 😂😂",
    "fantstic direction and music!!!"
]

data = []

for i in range(10000):

    name = random.choice(names)

    desc = random.choice(messy_descriptions)

    genre = random.choice(genres)

    data.append([name, desc, genre])

df = pd.DataFrame(data, columns=["name","description","genre"])

df.to_csv("movie_dataset_preprocessing_practice.csv", index=False)