import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

np.random.seed(42)

rows = 1000  # MASSIVE DATASET

age = np.random.randint(18, 65, rows)
income = np.random.randint(15000, 150000, rows)
time_on_site = np.random.randint(1, 120, rows)
ads_clicked = np.random.randint(0, 10, rows)
previous_purchases = np.random.randint(0, 20, rows)

# Logic for YES / NO (hidden rule)
bought = (
    (income > 50000) &
    (time_on_site > 30) &
    (ads_clicked > 2)
).astype(int)

df = pd.DataFrame({
    'age': age,
    'income': income,
    'time_on_site': time_on_site,
    'ads_clicked': ads_clicked,
    'previous_purchases': previous_purchases,
    'bought': bought
})

print(df)

x = df.drop('bought',axis=1)
y = df['bought']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)