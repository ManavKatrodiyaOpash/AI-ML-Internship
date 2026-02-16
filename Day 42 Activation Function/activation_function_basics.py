import numpy as np

z = np.array([-2, -1, 0, 1, 2])

# Sigmoid
sigmoid = 1 / (1 + np.exp(-z))

# ReLU
relu = np.maximum(0, z)

# Tanh
tanh = np.tanh(z)

print("Sigmoid:", sigmoid)
print("ReLU:", relu)
print("Tanh:", tanh)