import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

n=100
data = {
    "Age": np.random.randint(22,90,n),
    "Income": np.random.randint(25000,100000,n),
    "Loan_Approved": np.random.choice([0,1],n),
}

df = pd.DataFrame(data)

print(df)

x = df[['Age', 'Income']]
y = df['Loan_Approved']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=10,
)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print(accuracy*100,"%")