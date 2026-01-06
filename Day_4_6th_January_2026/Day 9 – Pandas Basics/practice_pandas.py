import numpy as np
import pandas as pd


data = {
    'Transaction_ID': range(101, 111),
    'Category': ['Electronics', 'Furniture', 'Electronics', 'Office', 'Furniture', 'Electronics', 'Office', 'Furniture', 'Office', 'Electronics'],
    'Sales': [250, 450, 150, 80, 700, 1200, 300, 450, 50, 900],
    'Region': ['North', 'South', 'East', 'West', 'North', 'East', 'South', 'West', 'North', 'East'],
    'Profit': [50, 100, -20, 10, 150, 300, 60, 90, 5, 200]
}

# Task 1: Load, explore, and manipulate a sales dataset using Pandas.
# Introduction In this task, you will create a mock dataset representing store transactions. You will practice the essential workflow of an analyst: inspecting the data quality, filtering for specific high-value targets, and organizing the information through sorting.
# Points to focus on:
# Use df.describe() and df.shape to understand the statistical distribution and dimensions of your data.
# Apply boolean indexing to filter rows where "Sales" are greater than a specific threshold and "Category" matches a certain criteria.
# Perform a multi-level sort (e.g., sort by "Region" alphabetically and then by "Profit" in descending order).

print("\nTask 1 :- \n \tLoad, explore, and manipulate a sales dataset using Pandas.\n\tPoints to focus on:Use df.describe() and df.shape to understand the statistical distribution and dimensions of your data.\n\tApply boolean indexing to filter rows where 'Sales' are greater than a specific threshold and 'Category' matches a certain criteria.Perform a multi-level sort (e.g., sort by 'Region' alphabetically and then by 'Profit' in descending order \n\n")

df = pd.DataFrame(data)
print(df)
print(f"\n\n DF.Describe :- \n{df.describe()}")
print(f"\n DF.shape = {df.shape}")

df['Boolean'] = np.where((df['Sales'] > 500) & (df['Region'] == "North"), "Yes", "No")
print(df)
print("\n\n")
print(df.sort_values(by="Profit", ascending=False))

# Task 2: Load a CSV file and perform a "health check" on the data.
# Introduction: Before analyzing data, you must understand its size and the type of information it contains.
# Points to focus on:
# Use pd.read_csv() to load 'day9_practice.csv'.
# Use df.shape to see how many rows and columns exist.
# Use df.columns to list all feature names and df.dtypes to see if they are integers, floats, or objects.

print("\nTask 2 :- \n \tLoad a CSV file and perform a 'health check' on the data.\n\tPoints to focus on: Use pd.read_csv() to load the file.\n\tCheck df.shape and df.dtypes to understand the data structure.\n\tUse df.head(3) to see the first few rows.\n\n")

print(f"All the column names :- {df.columns}")
print(f"All the dtypes :- {df.dtypes}")

# Task 3: Generate a statistical summary of numerical columns.
# Introduction: Data scientists use summary statistics to find the average, minimum, and maximum values across the dataset instantly.
# Points to focus on:
# Use df.describe() to get the mean, std, and quartiles for 'Sales' and 'Profit'.
# Use .value_counts() on the 'Category' column to see which category appears most often.
# Find the total sum of the 'Sales' column using df['Sales'].sum().

print("\nTask 3 :- \n \tGenerate a statistical summary of numerical columns.\n\tPoints to focus on: Use df.describe() for a statistical overview.\n\tUse .value_counts() on the 'Category' column to see frequency.\n\tCalculate the total sum of the 'Sales' column.\n\n")

print(f"DF.Describe :- \n{df.describe()}")
print(f"\nDF.value_counts :- \n{df.value_counts()}")
print(f"\n Total of all the sales is :- {df['Sales'].sum()}")

# Task 4: Extract specific subsets of data based on conditions.
# Introduction: Often, you only care about a specific group (e.g., only 'Electronics'). This task teaches you how to "slice" your data.
# Points to focus on:
# Create a new DataFrame called 'high_sales' that only contains rows where Sales > 500.
# Filter the data to show only transactions that happened in the 'North' region.
# Use the & operator to find rows where Category is 'Office' AND Profit is greater than 0.

print("\nTask 4 :- \n \tExtract specific subsets of data based on conditions.\n\tPoints to focus on: Filter rows where Sales > 500.\n\tFilter for 'North' region transactions only.\n\tCombine conditions using & to find profitable 'Office' items.\n\n")

print(df[df['Category'] == "Electronics"])

df2 = df[df['Sales'] > 500]
print(df2)

print(df[df['Region'] == "North"])
print(df[(df['Category'] == "Office") & (df['Sales'] > 0)])

# Task 5: Organize the dataset to find top performers.
# Introduction: Sorting allows you to quickly identify your most profitable items or your worst-performing regions.
# Points to focus on:
# Sort the DataFrame by 'Profit' in descending order (highest profit at the top).
# Perform a nested sort: Sort by 'Category' alphabetically, and then by 'Sales' from highest to lowest.
# Use .reset_index(drop=True) after sorting to keep the row numbers clean.

print("\nTask 5 :- \n \tOrganize the dataset to find top performers.\n\tPoints to focus on: Sort by 'Profit' in descending order.\n\tPerform a nested sort on 'Category' and 'Sales'.\n\tReset the index to keep the DataFrame organized after sorting.\n\n")

print(f"DataFrame by 'Profit' in descending order :- \n{df['Profit'].sort_values(ascending=False)}")
print(df.sort_values(by=["Category","Sales"], ascending=[True,False]))
df.reset_index(drop=True)
print(df)

# Task 6: Create new information and export your findings.
# Introduction: In this task, you will create a calculated column and save your filtered results to a new file.
# Points to focus on:
# Create a new column 'Profit_Margin' which is (Profit / Sales).
# Rename the 'Region' column to 'Location' using .rename().
# Save your final, filtered, and sorted DataFrame to a new file named 'filtered_sales.csv' using .to_csv().

print("\nTask 6 :- \n \tCreate new information and export your findings.\n\tPoints to focus on: Create a calculated 'Profit_Margin' column.\n\tRename 'Region' to 'Location'.\n\tSave the final result to a new CSV file.\n\n")

df2 = df.copy()
df2['Profit_Margin'] = df2['Profit'] / df['Sales']
df2['Region'].rename('Location', inplace=True)
print(df2)
df2.to_csv("Altered_data.csv", index=False)