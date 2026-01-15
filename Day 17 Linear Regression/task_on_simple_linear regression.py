import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

np.random.seed(42)

experience = np.arange(1, 101)
salary = 30000 + experience * 1500 + np.random.randint(-5000, 5000, 100)

df = pd.DataFrame({
    "Experience": experience,
    "Salary": salary
})

print(df)

# Task 1:
# Load the simple linear regression dataset and inspect it
print("Task 1: Load and inspect simple linear regression dataset")

# Task 2:
# Define Experience as feature and Salary as target
print("Task 2: Define X and y for simple linear regression")

# Task 3:
# Apply train-test split
print("Task 3: Perform train-test split")

# Task 4:
# Train a Linear Regression model
print("Task 4: Train simple linear regression model")

# Task 5:
# Predict salary for new experience value
print("Task 5: Predict salary using simple linear regression")

x = df[['Experience']]
y = df['Salary']

sns.regplot(x=x, y=y)
plt.title("Simple Linear Regression")
plt.tight_layout()
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

model.predict(x_test)
y_pred = model.predict(x_test)

sns.scatterplot(x=x_test['Experience'], y=y_test, label="Actual Value", color='blue')
sns.scatterplot(x=x_test['Experience'], y=y_pred, label="Predicted Value", color='red')
sns.lineplot(x=x_test['Experience'], y=y_pred, color='red')
plt.title("Actual vs Predicted Value")
plt.tight_layout()
plt.legend()
plt.show()
