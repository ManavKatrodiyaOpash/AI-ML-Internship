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