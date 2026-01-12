# =====================================
# CREATE A VERY MESSY DATASET FOR EDA
# =====================================

import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "Customer_ID": np.arange(1, 501),
    "Age": np.random.choice([18, 25, 30, 35, 40, 45, 50, None, 150, -5], 500),
    "Gender": np.random.choice(["Male", "Female", "M", "F", "male", None], 500),
    "Annual_Income": np.random.choice([20000, 30000, 50000, 70000, None, 999999], 500),
    "Spending_Score": np.random.choice([10, 20, 30, 40, 50, None, 120], 500),
    "City": np.random.choice(["Mumbai", "Delhi", "Ahmedabad", "Pune", "", None], 500),
    "Purchased": np.random.choice(["Yes", "No", "Y", "N", None], 500)
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv("messy_customer_data.csv", index=False)

print("Messy dataset created: messy_customer_data.csv")