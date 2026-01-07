import numpy as np
import pandas as pd

# Create 500 rows of messy data
np.random.seed(42)
n = 500
data = {
    'Date': np.random.choice(['2023-01-01', '01/05/2023', '2023-13-01', np.nan, '2023.06.01'], n),
    'Customer_Name': np.random.choice(['John Doe', 'john doe', ' J. Doe ', 'ALICE', 'Alice', 'Bob'], n),
    'Age': np.random.choice([25, 30, 200, -5, np.nan, 45, 12, 34], n),
    'City': np.random.choice(['New York', 'new york', 'NY', 'London', 'LNDN', np.nan, 'Paris '], n),
    'Product_ID': [f"PROD_{np.random.randint(100, 105)}" for _ in range(n)],
    'Price_USD': np.random.choice(['$100', '200', '150.5', 'Free', np.nan, '99999'], n),
    'Quantity': np.random.choice([1, 2, 10, 500, np.nan], n)
}

df = pd.DataFrame(data)
# Add some exact duplicates
df = pd.concat([df, df.iloc[:10]], ignore_index=True)
df.to_csv("dirty_dataset.csv", index=False)

print(df)
print("Dirty Dataset Created! Shape:", df.shape)
print(f"Null Values :- \n{df.isnull().sum()}")
print(f"Info :- {df.info()}")
print(f"Duplicate :- {df.duplicated().sum()}")

df.drop_duplicates(keep='first', inplace=True)
print(f"After dropping duplicates shape :- {df.shape}")

df['Customer_Name'] = df['Customer_Name'].str.strip().str.title()
df['City'] = df['City'].str.strip().str.title().replace({'Ny': 'New York', 'Lndn': 'London'})
df['Price_USD'] = df['Price_USD'].str.replace('$', '', regex=False).replace('Free', '0')
df['Price_USD'] = pd.to_numeric(df['Price_USD'], errors='coerce')
df.loc[df['Age'] > 100, 'Age'] = np.nan
df.loc[df['Age'] < 0, 'Age'] = np.nan
df.loc[df['Price_USD'] > 1000] = np.nan
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Price_USD'] = df['Price_USD'].fillna(df['Price_USD'].median())
df['Quantity'] = df['Quantity'].fillna(1) # Assumption: at least 1 bought
df['City'] = df['City'].fillna("unknown")

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# Drop rows where the date was completely invalid (like 13th month)
df = df.dropna(subset=['Date'])

df.fillna(df.mean(numeric_only=True), inplace=True)

print("\n--- FINAL CLEANING CHECK ---")
print("Dirty Dataset Created! Shape:", df.shape)
print(F"Describe :- \n{df.describe()}")
print(f"Null Values :- \n{df.isnull().sum()}")
print(f"Info :- {df.info()}")
print(f"Duplicate :- {df.duplicated().sum()}")

df.to_csv("cleaned_dataset.csv")