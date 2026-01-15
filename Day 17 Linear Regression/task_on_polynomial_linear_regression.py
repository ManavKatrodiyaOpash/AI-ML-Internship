import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split



np.random.seed(7)

x = np.linspace(-5, 5, 150)
y = 4 * x**2 + 3 * x + 10 + np.random.normal(0, 15, 150)

df = pd.DataFrame({
    "x": x,
    "y": y
})
print(df)

# Task 11:
# Load polynomial regression dataset and visualize curve
print("Task 1: Load polynomial regression dataset")

# Task 12:
# Apply PolynomialFeatures transformation
print("Task 2: Convert input feature into polynomial features")

# Task 13:
# Train Linear Regression model on polynomial data
print("Task 3: Train polynomial linear regression model")

# Task 14:
# Predict values using polynomial regression
print("Task 4: Predict numeric output using polynomial regression")

# Task 15:
# Compare linear vs polynomial regression performance
print("Task 5: Compare simple vs polynomial regression")

sns.regplot(x="x", y="y", data=df, order=2)
plt.tight_layout()
plt.show()

x=df[['x']]
y=df['y']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=7)

poly = PolynomialFeatures(degree=2, include_bias=False)

x_train_poly = poly.fit_transform(x_train)
x_test_poly = poly.transform(x_test)

model = LinearRegression()
model.fit(x_train_poly, y_train)

y_pred = model.predict(x_test_poly)
print(y_pred)

sns.scatterplot(x=x_test['x'],y=y_test,color='blue',label='Actual Value')
sns.scatterplot(x=x_test['x'],y=y_pred,color='red',label='Predicted Value')
sns.lineplot(x=x_test['x'],y=y_pred,color='red')
plt.title("Actual vs Predicted Value")
plt.tight_layout()
plt.legend()
plt.show()