import pandas as pd
import numpy as np
import random

np.random.seed(42)

rows = 1000

names = [f"Person_{i}" for i in range(1, rows + 1)]

ages = np.random.randint(18, 65, rows)
genders = np.random.choice(["Male", "Female"], rows)
bmi = np.round(np.random.uniform(18, 40, rows), 1)
smoker = np.random.choice(["Yes", "No"], rows, p=[0.3, 0.7])
chronic = np.random.choice([0, 1], rows, p=[0.7, 0.3])

# Risk Level (Classification target)
risk_level = []
for a, b, s, c in zip(ages, bmi, smoker, chronic):
    score = a * 0.3 + b * 0.6 + (15 if s == "Yes" else 0) + (20 if c == 1 else 0)
    if score > 70:
        risk_level.append("High")
    elif score > 45:
        risk_level.append("Medium")
    else:
        risk_level.append("Low")

# Insurance Cost (Regression target)
insurance_cost = (
        ages * 120 +
        bmi * 250 +
        np.where(smoker == "Yes", 8000, 0) +
        np.where(chronic == 1, 12000, 0) +
        np.random.randint(1000, 5000, rows)
)

df = pd.DataFrame({
    "Name": names,
    "Age": ages,
    "Gender": genders,
    "BMI": bmi,
    "Smoker": smoker,
    "ChronicDisease": chronic,
    "RiskLevel": risk_level,
    "InsuranceCost": insurance_cost
})

df.to_csv("chronic_desease.csv", index=False)
