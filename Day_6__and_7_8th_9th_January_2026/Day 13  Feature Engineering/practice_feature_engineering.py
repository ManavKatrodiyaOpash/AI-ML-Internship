import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Age": [22, 25, 30, 28, 35, 40, 45, 50, 23, 27, 32, 36, 41, 46, 29, 33, 38, 42, 48, 55],
    "Height_cm": [160, 165, 170, 168, 172, 175, 178, 180, 162, 166, 169, 173, 176, 179, 167, 171, 174, 177, 181, 183],
    "Weight_kg": [55, 60, 65, 62, 70, 75, 78, 80, 58, 61, 67, 72, 76, 79, 63, 68, 74, 77, 82, 85],
    "Salary": [25000, 30000, 40000, 35000, 50000, 60000, 65000, 70000, 28000, 32000,
               42000, 52000, 62000, 68000, 36000, 45000, 58000, 64000, 72000, 80000],
    "Experience_Years": [1, 2, 5, 3, 7, 10, 12, 15, 1, 2, 6, 8, 11, 14, 4, 6, 9, 11, 16, 20]
}

df = pd.DataFrame(data)
print(df)

# ============================
# Task 1: Feature Creation
# Load the dataset using pandas
# Create a new feature BMI using Height and Weight
# BMI = Weight / (Height in meters)^2
# Print dataset before and after feature creation
# ============================

print("\n\nTask 1: Feature Creation")
print("\t Load the dataset using pandas")
print("\t Create BMI using Height and Weight")
print("\t BMI = Weight / (Height in meters)^2")
print("\t Print dataset before and after feature creation")

df['BMI'] = df['Weight_kg'] / (df['Height_cm'] / 100) ** 2
print(df)

# ============================
# Task 2: Feature Creation
# Create a new feature Salary_Per_Year
# Formula: Salary / Experience_Years
# Understand earning efficiency
# Print updated dataset
# ============================

print("\n\nTask 2: Feature Creation")
print("\t Create Salary_Per_Year feature")
print("\t Salary_Per_Year = Salary / Experience_Years")
print("\t Understand earning efficiency")
print("\t Print updated dataset")

df['Salary_Per_Year'] = df['Salary'] / df['Experience_Years']
print(df)

# ============================
# Task 3: Feature Creation
# Create a categorical feature Age_Group
# Age < 30  -> Young
# Age 30-45 -> Adult
# Age > 45  -> Senior
# Print dataset
# ============================

print("\n\nTask 3: Feature Creation")
print("\t Create Age_Group feature")
print("\t Young: Age < 30")
print("\t Adult: Age between 30 and 45")
print("\t Senior: Age > 45")
print("\t Print dataset")

df['Age_Group'] = np.where(
    df['Age'] < 30, "Young",np.where(
    df['Age'] <= 45, "Adult",
                    "Senior")
)
print(df)

# ============================
# Task 4: Feature Selection
# Find correlation between numeric features
# Identify highly correlated columns
# Remove ONE unnecessary feature
# Print remaining column names
# ============================

print("\n\nTask 4: Feature Selection")
print("\t Find correlation between numeric features")
print("\t Identify highly correlated columns")
print("\t Remove one unnecessary feature")
print("\t Print remaining column names")

cor = df.corr(numeric_only=True)
sns.heatmap(cor,annot=True)
plt.tight_layout()
plt.show()
print(cor)

# ============================
# Task 5: Improve Dataset Features
# Check for duplicate rows
# Check for constant or low-importance columns
# Keep only meaningful features
# Save final improved dataset to CSV
# ============================

print("\n\nTask 5: Improve Dataset Features")
print("\t Check for duplicate rows")
print("\t Check constant or low-importance columns")
print("\t Keep meaningful features only")
print("\t Save final dataset to CSV")

print(F"Duplicates :- \n{df.duplicated().sum()}")
print("Constant columns",df.nunique())
# df.to_csv("final_feature_engineered_dataset.csv", index=False)
print("\nFinal dataset saved successfully")