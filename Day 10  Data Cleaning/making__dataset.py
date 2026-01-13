import pandas as pd
import numpy as np

# Generating a dataset with "mistakes" for cleaning practice
data = {
    'Employee_ID': [101, 102, np.nan, 104, 105, 106, 107, 108, np.nan, 110],
    'Department': ['Sales', 'IT', 'IT', 'HR', 'Sales', 'Marketing', 'HR', 'IT', 'Sales', 'Marketing'],
    'Priority_Level': ['Low', 'High', 'Medium', 'Low', 'High', 'Low', 'Medium', 'High', 'Low', 'Medium'],
    'Salary': [50000, 120000, 85000, 45000, np.nan, 60000, 55000, 110000, 48000, np.nan],
    'Experience_Years': [2, 10, 5, 1, 8, 3, 4, 9, 2, 6]
}

df = pd.DataFrame(data)
df.to_csv('dirty_data.csv', index=False)
print("File 'dirty_data.csv' has been created successfully!")