import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# sample data
data = {
    "height": [160, 170, 180],
    "weight": [60, 70, 80]
}

df = pd.DataFrame(data)

# create new feature
df["BMI"] = df["weight"] / (df["height"]/100)**2

print(df)



# find correlation
corr = df.corr()

# visualize
sns.heatmap(corr, annot=True)
plt.show()