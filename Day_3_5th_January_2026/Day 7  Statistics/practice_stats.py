import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import chi2

from statistic import covariance

# Dataset for tasks
data = {
    'Time': [5, 7, 8, 12, 15, 18, 20, 22, 25, 30, 45, 120],
    'Spent': [20, 25, 25, 50, 60, 70, 80, 90, 95, 110, 150, 500],
    'Device': ['M', 'M', 'M', 'D', 'D', 'D', 'D', 'D', 'D', 'T', 'T', 'T']
}
df = pd.DataFrame(data)
print(df)

# Task 1: Central Tendency & The "Outlier Effect"
# Task:
# Calculate the Mean and Median for "Amount Spent."
# Question: Why is the Mean so much higher than the Median? Which one better represents the "average" customer?

print(
    "\nTask 1: Central Tendency & The 'Outlier Effect':- \n \t Calculate the Mean and Median for 'Amount Spent.' \n \t Question: Why is the Mean so much higher than the Median? Which one better represents the 'average' customer?\n\n")

print(f"The mean of 'spent' table is :- {np.mean(df['Spent'])}")
print(f"The median of 'spent' table is :- {np.median(df['Spent'])}")

# Task 2: Dispersion & Standardizing
# Task:
# Calculate the Standard Deviation for "Time on Site." Calculate the Z-score for Customer 12 (the last row).
# Question: Based on the Z-score, would you statistically classify Customer 12 as an outlier? (Hint: Is |Z| > 3?)

print(
    "\nTask 2: Dispersion & Standardizing:- \n \t Calculate the Standard Deviation for 'Time on Site.' \n \t Calculate the Z-score for Customer 12. \n \t Question: Based on the Z-score, would you statistically classify Customer 12 as an outlier? (Hint: Is |Z| > 3?)\n\n")

print(f"The standard deviation of 'Time on Site' table is :- {np.std(df['Time']):.2f}")
cus_12 = df.iloc[-1]
cus_12_time = cus_12['Time']
mean_time = df['Time'].mean()
std_time = df['Time'].std()

cus_12_z_score = (cus_12_time - mean_time) / std_time

print(f"The z-score of the last customer is :- {cus_12_z_score:.2f}")

df['Time_Zscore'] = (df['Time'] - mean_time) / std_time
print(df)

# Task 3: Distribution & Shape
# Task:
# Calculate the Skewness of "Amount Spent."
# Question: Is the data right-skewed or left-skewed? Does the "tail" point toward the expensive purchases or the cheap ones?

print(
    "\nTask 3: Distribution & Shape:- \n \t Calculate the Skewness of 'Amount Spent.' \n \t Question: Is the data right-skewed or left-skewed? Does the 'tail' point toward the expensive purchases or the cheap ones?\n\n")

print(f"The skewness of the column amount spent is :- {df['Spent'].skew():.2f}")

# Task 4: Relationships
# Task:
# Calculate the Pearson Correlation (r) and Covariance between "Time on Site" and "Amount Spent."
# Question: Does spending more time on the site result in more money spent? How strong is that relationship?

print(
    "\nTask 4: Relationships:- \n \t Calculate the Correlation (Pearson’s r) between 'Time on Site' and 'Amount Spent.' \n \t Calculate the Covariance between them. \n \t Question: Does spending more time on the site result in more money spent? How strong is that relationship?\n\n")

cov = np.cov(df['Time'], df['Spent'])[0, 1]
corr = np.corrcoef(df['Time'], df['Spent'])[0, 1]
print(f"The covariance of the data 'Time' and 'Spent' is :- {cov:.2f}")
print(f"The correlation of the data 'Time' and 'Spent' is :- {corr:.2f}")

# Task 5: Categorical Analysis (Chi-Square)
# Task:
# Create a contingency table of Device Category vs Spending Level (e.g., "High" > $100 vs "Low" < $100). Run a Chi-Square test.
# Question: Is the amount spent dependent on the device used, or is it likely due to random chance?

print(
    "\nTask 5: Categorical Analysis (Chi-Square):- \n \t Create a contingency table of Device Category vs Spending Level (e.g., 'High Spenders' > $100 vs 'Low Spenders' < $100). \n \t Run a Chi-Square test. \n \t Question: Is the amount spent dependent on the device used, or is it likely due to random chance?\n\n")

df['Spending_Level'] = np.where(df['Spent'] > 100, "High", "Low")
print(df)
continguency_table = pd.crosstab(df['Device'], df['Spending_Level'])

chi2, p_val, dof, expected = stats.chi2_contingency(continguency_table)
print(f" The chi-square calculation is :- {chi2}")

# Task 6: Impact of Outlier Removal
# Task:
# Create a new version of your dataset (df_clean) by removing the outlier (Customer 12).
# Recalculate the Mean and Standard Deviation.
# Compare them to the original Mean/Std Dev.
# Why? In Data Science, we often remove outliers to create more "stable" models, but we must justify why we did it.

print(
    "\nTask 6: Impact of Outlier Removal:- \n \t Create a new version of your dataset (df_clean) by removing Customer 12. \n \t Recalculate the Mean and Standard Deviation and compare them to the original. \n \t Why? Identifying how much a single point shifts your 'truth' is vital for data integrity.\n\n")

another_df = df.drop(df.index[11])
print(another_df)
print(f"The new mean according to the new data is :- {np.mean(another_df['Spent']):.2f}")
print(f"The new standard deviation according to the new data is :- {np.std(another_df['Spent'])}")

print("\nThe comparision between old mean and new mean of 'Spent' is :- ")
print(f"\t Old mean of 'Spent' :- {np.mean(df['Spent']):.2f}")
print(f"\t New mean of 'Spent' :- {np.mean(another_df['Spent']):.2f}")
print(f"\t Difference :- {np.mean(another_df['Spent']) - np.mean(df['Spent']):.2f}")

print("\nThe comparision between old standard deviation and new standard deviation of 'Spent' is :- ")
print(f"\t Old standard deviation of 'Spent' :- {np.std(df['Spent']):.2f}")
print(f"\t New standard deviation of 'Spent' :- {np.std(another_df['Spent']):.2f}")
print(f"\t Difference :- {np.std(another_df['Spent']) - np.std(df['Spent']):.2f}")

# Task 7: The "Standardization" (Z-Score Scaling)
# Task:
# Create a new column 'Spent_Z' by standardizing the 'Spent' column.
# Verify that the mean of 'Spent_Z' is approximately 0 and the standard deviation is 1.
# Why? Machine Learning algorithms (like K-Means) require all features to be on the same scale (Z-Score scaling) to work properly.

print(
    "\nTask 7: The 'Standardization' (Z-Score Scaling):- \n \t Transform the 'Spent' column into Z-scores. \n \t Verify if the new mean is 0 and std dev is 1. \n \t Why? This process, called Scaling, is a mandatory step before feeding data into most AI models.\n\n")

another_df.drop(columns=['Time_Zscore'], inplace=True)
another_df['Spent_Z'] = (another_df['Spent'] - another_df['Spent'].mean())/another_df['Spent'].std()
print(another_df)
print(f"\nThe new column 'Spent_Z' mean is :- {another_df['Spent_Z'].mean():.2f}")
print(f"The new column 'Spent_Z' standard deviation is :- {another_df['Spent_Z'].std():.2f}")

# Task 8: Coefficient of Variation (CV)
# Task:
# Calculate the CV for 'Time' and 'Spent' (Formula: (Std Dev / Mean) * 100).
# Compare the two. Which variable has higher relative variability?
# Why? Standard Deviation is hard to compare when units are different (minutes vs dollars). CV makes them comparable by turning them into percentages.

print(
    "\nTask 8: Coefficient of Variation (CV):- \n \t Calculate (Std Dev / Mean) * 100 for both Time and Spent. \n \t Compare which one is more 'volatile' relative to its average. \n \t Why? This allows you to compare the spread of 'Apples' and 'Oranges'.\n\n")

print(f"The original DF is :- \n{df}")
cv_time = (df['Time'].std() / df['Time'].mean()) * 100
cv_spent = (df['Spent'].std() / df['Spent'].mean()) * 100
print(f"\nThe CV of 'Time' is :- {cv_time:.2f}")
print(f"The CV of 'Spent' is :- {cv_spent:.2f}")
print(f"The difference between these two CV is :- {cv_time - cv_spent:.2f}")

# Task 9: Percentiles and IQR (The Boxplot Math)
# Task:
# Calculate the 25th (Q1) and 75th (Q3) percentiles for 'Spent'.
# Calculate the IQR (Q3 - Q1).
# Define an outlier as any value > Q3 + (1.5 * IQR). Does Customer 12 still qualify?
# Why? This is the mathematical logic used to draw 'Boxplots' and find outliers without using Z-scores.

print(
    "\nTask 9: Percentiles and IQR (The Boxplot Math):- \n \t Calculate Q1, Q3, and the Interquartile Range (IQR). \n \t Use the 1.5*IQR rule to mathematically detect outliers. \n \t Why? This is the most common industry standard for identifying 'Bad Data'.\n\n")


Q1 = df['Spent'].quantile(0.25)
Q3 = df['Spent'].quantile(0.75)
IQR = Q3 - Q1

print(f"The 75th percentile (Q3) is :- {Q3:.2f}")
print(f"The 25th percentile (Q3) is :- {Q1:.2f}")
print(f"The difference between them (Q3-Q1) is :- {Q3- Q1:.2f}")