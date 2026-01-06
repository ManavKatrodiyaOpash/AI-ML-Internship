import pandas as pd

df = pd.read_csv("dirty_data.csv")

print(df)
print(f"data.shape = {df.shape}")
print(f"missing values :- \n{df.isnull().sum()}")
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Employee_ID'] = df['Employee_ID'].interpolate().astype(int)
print(df)
print(f"missing values :- \n{df.isnull().sum()}")
df = pd.get_dummies(df, columns=['Salary'])
print(df)