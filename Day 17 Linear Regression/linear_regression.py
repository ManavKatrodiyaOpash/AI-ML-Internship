import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [30000, 35000, 40000, 45000, 50000]
}

df = pd.DataFrame(data)
print(df)

x = df[["Experience"]]
y = df["Salary"]

sns.scatterplot(x="Experience", y="Salary",data=df)
sns.lineplot(x="Experience", y="Salary",data=df)
plt.tight_layout()
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)

print(y_pred)
print(accuracy*100)