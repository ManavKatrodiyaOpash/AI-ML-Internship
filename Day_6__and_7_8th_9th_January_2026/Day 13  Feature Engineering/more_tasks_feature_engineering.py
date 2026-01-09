import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.external.qt_loaders import QT_API_PYQTv1

np.random.seed(10)

# ============================
# Realistic Mixed-Type Dataset
# (60 Rows with Numeric + Categorical Data)
# ============================

data = {
    "Age": np.random.randint(18, 60, 60),
    "Gender": np.random.choice(["Male", "Female"], 60),
    "Department": np.random.choice(["IT", "HR", "Sales", "Finance", "Marketing"], 60),
    "Education_Level": np.random.choice(["High School", "Bachelor", "Master", "PhD"], 60),
    "Height_cm": np.random.randint(150, 190, 60),
    "Weight_kg": np.random.randint(45, 100, 60),
    "Monthly_Salary": np.random.randint(15000, 90000, 60),
    "Experience_Years": np.random.randint(0, 25, 60),
    "Working_Hours": np.random.randint(30, 70, 60),
    "Commute_KM": np.random.randint(1, 40, 60),
    "Remote_Work": np.random.choice(["Yes", "No"], 60),
    "Performance_Score": np.random.randint(1, 10, 60)
}

df = pd.DataFrame(data)
print(df)
print("\nDataset Shape:", df.shape)
print(f"Columns of dataset :- \n{df.columns}")

# ============================
# Task 1: Categorical Encoding
# Identify categorical features
# Apply One-Hot Encoding on Department
# Apply Label Encoding on Education_Level
# Print updated dataset
# ============================

print("\nTask 1: Categorical Encoding")
print("\t Identify categorical features")
print("\t Apply One-Hot Encoding on Department")
print("\t Apply Label Encoding on Education_Level")
print("\t Print updated dataset")

print(pd.crosstab(df["Department"], df["Education_Level"], margins=True))
df = pd.get_dummies(df, columns=["Department"],drop_first=True)

education_map = {
    "High School": 0,
    "Bachelor": 1,
    "Master": 2,
    "PhD": 3
}

df["Education_Level"] = df["Education_Level"].map(education_map)
print(df['Education_Level'])

# ============================
# Task 2: Binary Feature Engineering
# Convert Gender to binary format
# Convert Remote_Work to binary format
# Print updated dataset
# ============================

print("\nTask 2: Binary Feature Engineering")
print("\t Convert Gender to binary")
print("\t Convert Remote_Work to binary")
print("\t Print updated dataset")

df['Gender'] = np.where(df['Gender'] == "Male",1,0)
df['Remote_Work'] = np.where(df['Remote_Work'] == "Yes",1,0)
print(df)

# ============================
# Task 3: Advanced Feature Creation
# Create BMI feature
# Create Work_Intensity = Working_Hours / Experience_Years
# Handle division by zero
# Print dataset
# ============================

print("\nTask 3: Advanced Feature Creation")
print("\t Create BMI feature")
print("\t Create Work_Intensity feature")
print("\t Handle division by zero")
print("\t Print dataset")

df['BMI'] = df['Weight_kg']/(df['Height_cm']/100)**2
df['Work_Intensity'] = df['Working_Hours']/df['Experience_Years'].replace(0, np.nan)
print(df)

# ============================
# Task 4: Feature Transformation
# Apply log transformation on Monthly_Salary
# Create Age_Group feature (Young, Adult, Senior)
# Drop original columns if required
# ============================

print("\nTask 4: Feature Transformation")
print("\t Apply log transformation on Monthly_Salary")
print("\t Create Age_Group feature")
print("\t Drop original columns if required")

df['log_on_salary'] = np.log(df['Monthly_Salary'])
df['Age_Group'] = np.where(df['Age'] < 30,"Young",np.where(df['Age'] <=45,"Adult","Senior"))
print(df)

# ============================
# Task 5: Feature Selection
# Find correlation between numeric features
# Remove redundant numeric features
# Justify why a feature is removed
# ============================

print("\nTask 5: Feature Selection")
print("\t Find correlation between numeric features")
print("\t Remove redundant features")
print("\t Justify feature removal")

corr = df.corr(numeric_only=True)
sns.heatmap(corr,annot=True)
plt.tight_layout()
plt.show()

# Example: remove Height_cm if highly correlated with Weight_kg
# df.drop(columns=['Height_cm'], inplace=True)
print(df)

# ============================
# Task 6: Outlier Detection
# Detect outliers using IQR method
# Create Outlier_Flag column
# Do NOT delete rows
# ============================

print("\nTask 6: Outlier Detection")
print("\t Detect outliers using IQR")
print("\t Create Outlier_Flag feature")
print("\t Do not delete rows")

numeric_df = df.select_dtypes(include=["number"])

Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)
IQR = Q3 - Q1

df["Outlier_Flag"] = (( numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))).any(axis=1)
print(df["Outlier_Flag"].value_counts())
print(df)

# ============================
# Task 7: Final Dataset Optimization
# Remove constant or low-importance columns
# Reorder features logically
# Save final engineered dataset to CSV
# ============================

print("\nTask 7: Final Dataset Optimization")
print("\t Remove constant or low-importance columns")
print("\t Reorder features logically")
print("\t Save final engineered dataset to CSV")

constant_cols = [col for col in df.columns if df[col].nunique() == 1]
df.drop(columns=constant_cols, inplace=True)
print(df)
# df.to_csv("final_dataset.csv")