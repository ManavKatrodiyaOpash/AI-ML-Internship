from pickle import FALSE

import numpy as np
import pandas as pd
from scipy import stats

data = [22,25,25,27,45,10,15,39,100]

df = pd.Series(data)

print(df)

mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data, keepdims=True).mode[0]

cov = np.cov(data)
var = np.var(data)
std = np.std(data)

print(f"Mean: {mean} | Median: {median} | Mode: {mode}")
print(f"Std Dev: {std:.2f} | Variance: {var:.2f}")

# Calculate Z-scores for every point in our data
z_scores = stats.zscore(data)

# Detect outliers (standard threshold is |Z| > 3)
outliers = [data[i] for i in range(len(z_scores)) if abs(z_scores[i]) > 2] # Using 2 for small dataset
print(f"Potential Outliers: {outliers}")

skewness = stats.skew(data)
print(f"Skewness: {skewness:.2f}")
# A positive value means the 'tail' is on the right (affected by the '100' outlier).