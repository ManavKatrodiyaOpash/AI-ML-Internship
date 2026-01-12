import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# Part 1: Python Core & Logic
# ==========================================
print("\n" + "="*40 + "\nPart 1: Python Core & Logic\n" + "="*40)

# Task 1:- List Comprehension:
#       Given a list of numbers , create a new list containing the squares of only the even numbers using a single line of code.

print("\n Task 1 :- List Comprehension: \n\t\tGiven a list of numbers , create a new list containing the squares of only the even numbers using a single line of code.\n")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = [c**2 for c in nums if c%2==0]
print(ans)

# Task 2 :- Dictionary Manipulation:
#       Create a dictionary of 5 students and their marks. Write a function that returns the name of the student with the highest marks.

print("\n Task 2 :- Dictionary Manipulation: \n\t\t Create a dictionary of 5 students and their marks. Write a function that returns the name of the student with the highest marks.\n")

stu_data = {
    "stu_1" : 45,
    "stu_2" : 65,
    "stu_3" : 80,
    "stu_4" : 50,
    "stu_5" : 10,
}

high_stu = max(stu_data, key=stu_data.get)
print(f"The student who has highest marks is {high_stu} with {stu_data[high_stu]} marks.")

# Task 3 :- Lambda & Map:
#      Use a lambda function with map() to convert a list of temperatures in Celsius to Fahrenheit.

print("\n Task 3 :- Lambda & Map: \n\t\tUse a lambda function with map() to convert a list of temperatures in Celsius to Fahrenheit.\n")

cels = [0, 20, 37, 100]
print(cels)
farnht = list(map(lambda x: x*(9/5)+32,cels))
print(farnht)

# Task 4 :- File I/O:
#      Write a script that creates a text file named test.txt, writes "Python for Data Science" into it, then reads the file and counts the number of words.

print("\n Task 4 :- File I/O: \n\t\tWrite a script that creates a text file named test.txt, writes 'Python for Data Science' into it, then reads the file and counts the number of words.\n")

with open("test.txt","w") as f:
    f.write("Python for Data Science\n")

with open("test.txt", "r") as f:
    content = f.read()
    words = content.split()
    word_count = len(words)


# ==========================================
# PART 2: NumPy & Statistics
# ==========================================
print("\n" + "="*40 + "\nPart 2: NumPy & Statistics\n" + "="*40)

# Task 5 :- NumPy Basics:
#       Create a 3x3 matrix with values ranging from 1 to 9.
#       Replace all odd numbers in the matrix with -1.
print("\nTask 5 :- NumPy Basics: \n\t\tCreate a 3x3 matrix (1-9) and replace odd numbers with -1.\n")


vals = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(vals)

for i in range(3):
    for j in range(3):
        if vals[i][j] % 2 == 0:
            vals[i][j] = -1

print(vals)
# also can be done with vals[vals %2 != 0] = -1

# Task 6 :- Matrix Math:
#       Create two random 2x2 matrices and perform:
#       1. Element-wise multiplication. 2. Dot product.
print("\nTask 6 :- Matrix Math: \n\t\tPerform element-wise and dot product on random 2x2 matrices.\n")

arr1 = np.random.randint(1,10,(2,2))
print(f"array 1 :- \n{arr1}")
arr2 = np.random.randint(1,10,(2,2))
print(f"array 2 :- \n{arr2}")

print("\nElement-wise Multiplication:")
print(np.multiply(arr1, arr2))
print("\nDot Product:")
print(np.dot(arr1, arr2))

# Task 7 :- Stats Calculation:
#       data = [12, 15, 12, 15, 12, 100, 18, 15]. Calculate Mean/Median.
#       Identify the outlier and explain its effect on Mean vs Median.
print("\nTask 7 :- Stats Calculation: \n\t\tCalculate Mean/Median and explain outlier impact.\n")

data = [12, 15, 12, 15, 12, 100, 18, 15]
print(data)
print(f"Mean of data :- {np.mean(data)}")
print(f"Median of data :- {np.median(data)}")
print(f"Standard Deviation of data :- {np.std(data)}")

plt.boxplot(data)
plt.title("Boxplot Before removing outlier")
plt.tight_layout()
plt.show()

print("Removing outlier")
Q1 = np.quantile(data, 0.25)
Q3 = np.quantile(data, 0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

filtered_data = [c for c in data if c >=lower_bound and c<=upper_bound]
print(f"Filtered data after removing outlier :- {filtered_data}")

plt.boxplot(filtered_data)
plt.title("Boxplot After removing outlier")
plt.tight_layout()
plt.show()

# Task 8 :- Standardization:
#       Write the code/formula for Z-score normalization (Mean=0, Std=1).
print("\nTask 8 :- Standardization: \n\t\tImplement or explain Z-score normalization.\n")

data = [12, 15, 12, 15, 12, 100, 18, 15]

mu = np.mean(data)
sigma = np.std(data)

standardized_data = (data-mu)/sigma

new_mean = np.mean(standardized_data)
new_std = np.std(standardized_data)

print(f"Original Data: {data}")
print(f"Standardized Data: \n{standardized_data}")
print("-" * 30)
print(f"New Mean (should be ~0): {round(new_mean, 2)}")
print(f"New Std Dev (should be 1): {new_std}")

sns.kdeplot(data=data)
plt.tight_layout()
plt.show()

sns.kdeplot(data=standardized_data)
plt.tight_layout()
plt.show()

# ==========================================
# PART 3: Pandas & Data Cleaning
# ==========================================
print("\n" + "="*40 + "\nPart 3: Pandas & Data Cleaning\n" + "="*40)

data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivan', 'Jack'],
    'Age': [25, 30, 45, np.nan, 22, 65, 35, 62, 28, 40],
    'City': ['New York', 'London', 'New York', 'Paris', 'London', 'New York', 'Paris', 'London', 'New York', 'Paris'],
    'Department': ['Sales', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'HR', 'IT', 'Sales', 'HR'],
    'Monthly_Sales': [5000, 7000, 5500, 4000, 9000, 35000, 6200, 25000, 4800, 5100], # Note the outliers!
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Male']
}

df = pd.DataFrame(data)
print(df)

# Task 9 :- Filtering:
#       Filter rows where 'Age' > 25 and 'City' is 'New York' in a sample DataFrame.
print("\nTask 9 :- Filtering: \n\t\tFilter DataFrame by Age and City.\n")

print(df[(df['Age'] > 25) & (df['City'] == "New York")])

# Task 10 :- Handling Missing Values:
#       1. Check for nulls. 2. Fill numerical nulls with mean. 3. Drop rows with missing target.
print("\nTask 10 :- Handling Missing Values: \n\t\tDemonstrate null checking, filling, and dropping.\n")

print(df.isnull().sum())
df.fillna(df.mean(numeric_only=True), inplace=True)
print(df)

# Task 11 :- Grouping:
#       Find the total revenue per 'Product Category' from a Sales DataFrame.
print("\nTask 11 :- Grouping: \n\t\tCalculate total revenue per category using groupby.\n")

dept_sales = df.groupby('Department')['Monthly_Sales'].sum()
print(dept_sales)

# Task 12 :- Encoding:
#       Apply One-Hot Encoding to a 'Gender' column (Male, Female, Other).
print("\nTask 12 :- Encoding: \n\t\tApply One-Hot Encoding using pd.get_dummies().\n")

encoded_df = pd.get_dummies(df, columns=['Gender'])
print(encoded_df.head())


# ==========================================
# PART 4: EDA & Pipeline
# ==========================================
print("\n" + "="*40 + "\nPart 4: EDA & Pipeline\n" + "="*40)

# Task 13 :- Visualization Logic:
#       Write which plots are best for: 1. Distribution 2. Relationships 3. Outliers.
print("\nTask 13 :- Visualization: \n\t\tIdentify best plots for distribution, relationship, and outliers.\n")

# Task 14 :- Correlation:
#       Generate a Heatmap of the correlation matrix for a DataFrame.
print("\nTask 14 :- Correlation: \n\t\tGenerate and plot a correlation heatmap.\n")

cor = df.corr(numeric_only=True)
sns.heatmap(cor, annot=True)
plt.tight_layout()
plt.show()

# Task 15 :- Feature Engineering:
#       Create 'Is_Senior' column (1 if Age >= 60, else 0).
print("\nTask 15 :- Feature Engineering: \n\t\tCreate a conditional feature 'Is_Senior'.\n")

df['Is_Senior'] = np.where(df['Age'] >= 60, 1, 0)
print(df[['Name', 'Age', 'Is_Senior']])

# Task 16 :- The Pipeline Concept:
#       Describe the 5-step process from Raw Data to Model-Ready data.
print("\nTask 16 :- Pipeline: \n\t\tDescribe the 5-step data preprocessing pipeline.\n")