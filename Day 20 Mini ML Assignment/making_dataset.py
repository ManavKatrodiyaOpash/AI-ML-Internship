import numpy as np
import pandas as pd

np.random.seed(42)

n = 50000

df = pd.DataFrame({
    "EmployeeID": range(1, n+1),
    "Age": np.random.randint(21, 60, n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "Education": np.random.choice(["Bachelor", "Master", "PhD"], n),
    "Department": np.random.choice(["IT", "HR", "Finance", "Sales"], n),
    "JobRole": np.random.choice(["Engineer", "Manager", "Analyst"], n),
    "YearsExperience": np.random.randint(0, 35, n),
    "YearsAtCompany": np.random.randint(0, 30, n),
    "PerformanceScore": np.random.randint(1, 6, n),
    "WorkHours": np.random.randint(30, 70, n),
    "Overtime": np.random.choice(["Yes", "No"], n),
    "ProjectsHandled": np.random.randint(1, 20, n),
    "TrainingHours": np.random.randint(0, 100, n),
    "WorkLifeBalance": np.random.randint(1, 5, n),
    "JobSatisfaction": np.random.randint(1, 6, n),
    "Absences": np.random.randint(0, 20, n),
    "Promotions": np.random.randint(0, 5, n),
    "DistanceFromHome": np.random.randint(1, 50, n),
    "StressLevel": np.random.choice(["Low", "Medium", "High"], n)
})

# Salary (Regression Target)
df["MonthlyIncome"] = (
    20000
    + df["YearsExperience"] * 1500
    + df["PerformanceScore"] * 2000
    + np.random.randint(-5000, 5000, n)
)

# Attrition (Classification Target)
df["Attrition"] = np.where(
    (df["JobSatisfaction"] <= 2) |
    (df["WorkLifeBalance"] <= 2) |
    (df["StressLevel"] == "High"),
    "Yes", "No"
)

# Inject missing values
for col in ["Age", "MonthlyIncome", "WorkHours"]:
    df.loc[df.sample(frac=0.05).index, col] = np.nan

# Save dataset
df.to_csv("dataset.csv", index=False)

print("Dataset created:", df.shape)

# import kagglehub
#
# # Download latest version
# path = kagglehub.dataset_download("pavansubhasht/ibm-hr-analytics-attrition-dataset")
#
# print("Path to dataset files:", path)