from sklearn.model_selection import train_test_split
import pandas as pd

# Simple dataset
df = pd.DataFrame({
    "Age": [18, 19, 20, 21, 22],
    "Purchased": [0, 1, 0, 1, 1]
})

X = df[["Age"]]
y = df["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

print("Training data:")
print(X_train)

print("\nTesting data:")
print(X_test)