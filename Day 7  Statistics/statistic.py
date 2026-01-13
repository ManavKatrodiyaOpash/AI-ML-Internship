from statistics import covariance

import numpy as np
from scipy import stats

data = np.random.randint(10, 100, size=10)
print(data)

print(f"Mean of data is :- {np.mean(data)}")
print(f"Median of data is :- {np.median(data)}")
print(f"Mode of data is :- {stats.mode(data, keepdims=True).mode[0]}")
print(f"Variance of data is :- {np.var(data):.2f}")
print(f"Standard Deviation of data is :- {np.std(data):.2f}")


data = np.random.randint(10, 100, size=(4,5))
print(data)

print(f"Mean of data is :- {np.mean(data)}")
print(f"Median of data is :- {np.median(data)}")
print(f"Mode of data is :- {stats.mode(data).mode[0]}")
print(f"Variance of data is :- {np.var(data):.2f}")
print(f"Standard Deviation of data is :- {np.std(data):.2f}")


import numpy as np
import pandas as pd
from scipy import stats

# 1. Create Data
hours = [2, 3, 3, 4, 5, 6, 7, 8, 9, 20]
scores = [65, 70, 70, 75, 80, 85, 90, 95, 98, 100]

mean = np.mean(hours)
median = np.median(hours)
mode = stats.mode(hours)
skewness = stats.skew(hours)
kurtosis = stats.kurtosis(hours)
covariance = np.cov(hours,scores)[0][1]
corrleation = np.corrcoef(hours,scores)[0][1]
z_score = stats.zscore(hours)

print(f"Mean is :- {mean}")
print(f"Median is :- {median}")
print(f"Mode is :- {mode}")
print(f"Skewness is :- {skewness}")
print(f"Kurtosis is :- {kurtosis}")
print(f"Covariance is :- {covariance}")
print(f"Correlation is :- {corrleation}")
print(f"Z-score is :- {z_score}")