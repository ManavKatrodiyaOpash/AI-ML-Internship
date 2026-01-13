import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Create a simple dataset
data = {
    "StudyHours": [1, 2, 3, 4, 5, 6],
    "Pass": [0, 0, 0, 1, 1, 1]   # LABEL
}

df = pd.DataFrame(data)

# Features (input)
X = df[["StudyHours"]]

# Target (output)
y = df["Pass"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)

print(accuracy*100,"%")