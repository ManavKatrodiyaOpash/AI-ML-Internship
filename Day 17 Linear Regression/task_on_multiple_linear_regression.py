import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

np.random.seed(10)

data = {
    "Area_sqft": np.random.randint(500, 3000, 200),
    "Bedrooms": np.random.randint(1, 6, 200),
    "Distance_km": np.random.randint(1, 30, 200)
}

price = (
        data["Area_sqft"] * 120 +
        data["Bedrooms"] * 50000 -
        data["Distance_km"] * 2000 +
        np.random.randint(-30000, 30000, 200)
)

df = pd.DataFrame(data)
df["Price"] = price
print(df)

# Task 6:
# Load the multiple linear regression dataset
print("Task 1: Load multiple linear regression dataset")

# Task 7:
# Define multiple features and single target
print("Task 2: Define X (multiple features) and y")

# Task 8:
# Train Linear Regression model on multiple features
print("Task 3: Train multiple linear regression model")

# Task 9:
# Analyze coefficients to understand feature impact
print("Task 4: Analyze feature importance using coefficients")

# Task 10:
# Predict house price for new input values
print("Task 5: Predict house price using multiple linear regression")

x = df[['Area_sqft', 'Bedrooms', 'Distance_km']]
y = df['Price']

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
sns.regplot(data=df, x='Area_sqft', y='Price', ax=axes[0])
sns.regplot(data=df, x='Bedrooms', y='Price', ax=axes[1])
sns.regplot(data=df, x='Distance_km', y='Price', ax=axes[2])
plt.tight_layout()
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=40)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)