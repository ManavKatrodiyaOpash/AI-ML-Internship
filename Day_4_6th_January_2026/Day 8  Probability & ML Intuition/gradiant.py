import numpy as np
import matplotlib.pyplot as plt

# 1. Define our "Hill" (The Cost Function: f(x) = x^2)
def cost_function(x):
    return x**2

# 2. Define the Slope (The Gradient/Derivative: f'(x) = 2x)
def gradient(x):
    return 2*x

# 3. Gradient Descent Parameters
current_pos = 4      # Starting point on the hill
learning_rate = 0.1  # Step size
steps = 20           # How many steps to take

history = [current_pos]

# The "Walking" Loop
for _ in range(steps):
    # Calculate which way is down and take a step
    current_pos = current_pos - (learning_rate * gradient(current_pos))
    history.append(current_pos)

# 4. Visualization
x_vals = np.linspace(-5, 5, 100)
plt.plot(x_vals, cost_function(x_vals), color='gray', label='Error Landscape')
plt.scatter(history, [cost_function(x) for x in history], color='red', s=30)
plt.plot(history, [cost_function(x) for x in history], color='red', linestyle='--')
plt.title("Gradient Descent: Walking to the Minimum")
plt.xlabel("Weight (Parameter)")
plt.ylabel("Error (Loss)")
plt.legend()
plt.show()

print(f"Final position (minimum error): {current_pos:.4f}")

import numpy as np
import matplotlib.pyplot as plt

# 1. Create the "Hill" (Loss Function)
# Generate 100 points between -10 and 10 to draw the curve
x_curve = np.linspace(-10, 10, 100)
print(x_curve)
y_curve = x_curve**2

# 2. Gradient Descent Settings
x_start = 10
lr = 0.1
history_x = [x_start]
history_y = [x_start**2]

# 3. Run the "Walking" logic
x = x_start
for _ in range(10):
    slope = 2 * x
    x = x - (lr * slope)
    history_x.append(x)
    history_y.append(x**2)

# 4. Visualization
plt.figure(figsize=(10, 6))
plt.plot(x_curve, y_curve, color='gray', label='Loss Function (Hill)')
plt.scatter(history_x, history_y, color='red', label='Optimizer Steps')
plt.plot(history_x, history_y, color='red', linestyle='--') # Connect the dots

plt.title("Visualizing Gradient Descent: Walking Down the Hill")
plt.xlabel("Weight (x)")
plt.ylabel("Error (Loss)")
plt.legend()
plt.show()