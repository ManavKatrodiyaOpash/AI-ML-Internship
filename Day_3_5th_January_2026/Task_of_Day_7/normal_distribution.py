import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate data
data = np.random.normal(loc=0, scale=1, size=1000)
print(data)

# Plot histogram
plt.hist(data, bins=30, edgecolor='black', density=True)

# Plot theoretical PDF
x = np.linspace(-4, 4, 200)
pdf = norm.pdf(x, loc=0, scale=1)
plt.plot(x, pdf, label="Theoretical PDF")

plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True)
plt.legend()
plt.show()