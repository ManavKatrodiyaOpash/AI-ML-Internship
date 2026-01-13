import pandas as pd
from unicodedata import category

df = pd.read_csv("dirty_data.csv")

print(df)

# Task 1 : Locate missing data and remove incomplete records.
# Introduction: Before filling gaps, you must know where they are. In this task, you will find NaNs and remove rows that are too empty to be useful.
# Points to focus on:
# Use df.isnull().sum() to get a count of missing values per column.
# Use df.dropna(subset=['Critical_Column']) to remove rows where a specific important column is empty.
# Check the shape of the DataFrame before and after dropping to see how much data was lost.

print("\nTask 1 :- \n \tLocate missing data and remove incomplete records.\n\tPoints to focus on: Use df.isnull().sum() to count missing values.\n\tUse df.dropna() to remove rows with missing critical information.\n\tCompare df.shape before and after the drop.\n\n")

df1 = df.copy()
print(f"data.shape before droping missing value row= {df1.shape}")
print(f"\nmissing values :- \n{df1.isnull().sum()}")
df1 = df1.dropna()
print(f"\nmissing values :- \n{df1.isnull().sum()}")
print(f"\ndata.shape after droping missing value row= {df1.shape}")


# Task 2 : Fill missing numerical values using statistical measures.
# Introduction: Instead of throwing data away, we fill gaps with the mean or median so we keep the rest of the row's information.
# Points to focus on:
# Calculate the mean of a numerical column.
# Use df['Column'].fillna(mean_value, inplace=True) to plug the holes.
# Verify that df.isnull().sum() for that column is now 0.

print("\nTask 2 :- \n \tFill missing numerical values using statistical measures.\n\tPoints to focus on: Calculate the mean or median of a column.\n\tUse .fillna() to replace NaN values with your calculated average.\n\tVerify the column is now clean.\n\n")

df2 = df.copy()
print(f"Mean of every column that are numeric :- \n{df2.mean(numeric_only=True)}\n\n")
df2.fillna(df2.mean(numeric_only=True), inplace=True)
print(df2.isnull().sum())


# Task 3 : Convert unordered text categories into binary columns.
# Introduction: For categories like 'Color' or 'Category', we use One-Hot Encoding to create separate columns for each type.
# Points to focus on:
# Use pd.get_dummies(df, columns=['Category_Column']) on the dataset.
# Observe how the number of columns increases in your DataFrame.
# Ensure the new columns contain only 0s and 1s.

print("\nTask 3 :- \n \tConvert unordered text categories into binary columns.\n\tPoints to focus on: Use pd.get_dummies() on a categorical column.\n\tObserve the expansion of columns in the DataFrame.\n\tCheck the head of the data to see the new 0 and 1 values.\n\n")

df3 = df.copy()
categorical_cols = df3.select_dtypes(include='object').columns
df3 = pd.get_dummies(df3, columns=categorical_cols)
print(df3)

# Task 4 : Map ordered categories to numerical ranks.
# Introduction: For data with a natural order (e.g., Low, Medium, High), we assign specific numbers (0, 1, 2).
# Points to focus on:
# Define a dictionary: mapping = {'Low': 0, 'Medium': 1, 'High': 2}.
# Use df['Column'].map(mapping) to transform the text into numbers.
# Check that the data type of the column has changed from 'object' to 'int'.

print("\nTask 4 :- \n \tMap ordered categories to numerical ranks.\n\tPoints to focus on: Create a dictionary for mapping text to numbers.\n\tUse .map() to apply the transformation.\n\tVerify the data type change in the column.\n\n")

df4 = df.copy()
print(df4['Priority_Level'].map({'Low': 0, 'Medium': 1, 'High': 2}))

# Task 5 : Normalize numerical data to a 0-1 range.
# Introduction: This ensures that columns with large numbers don't dominate your machine learning model.
# Points to focus on:
# Implement the formula: (x - x.min()) / (x.max() - x.min()).
# Apply this formula to a column with large values (like Salary or Price).
# Use df.describe() to confirm the min is 0.0 and the max is 1.0.

print("\nTask 5 :- \n \tNormalize numerical data to a 0-1 range.\n\tPoints to focus on: Use the Min-Max formula to scale a numerical column.\n\tEnsure all values fall between 0 and 1.\n\tUse df.describe() to verify the new distribution.\n\n")

df5 = df.copy()
df5['Salary'] = df5['Salary'].fillna(df5['Salary'].mean())

# Instead of the loop:
df5['Salary'] = (df5['Salary'] - df5['Salary'].min()) / (df5['Salary'].max() - df5['Salary'].min())
print(df5['Salary'].describe()) # Check if min=0 and max=1