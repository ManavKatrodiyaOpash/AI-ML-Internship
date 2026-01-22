import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1200

data = {
    "Age": np.random.randint(18, 65, rows),
    "Salary": np.random.randint(20000, 150000, rows),
    "Experience": np.random.randint(0, 40, rows),
    "CreditScore": np.random.randint(300, 850, rows),
    "LoanAmount": np.random.randint(50000, 500000, rows),
    "Purchased": np.random.randint(0, 2, rows),          # Classification
    "HousePrice": np.random.randint(1000000, 10000000, rows)  # Regression
}

df = pd.DataFrame(data)
df.to_csv("xgboost_big_dataset.csv", index=False)