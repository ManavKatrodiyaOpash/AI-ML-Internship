# Task 1: The "Slow and Steady" Learner
# Start at x = 20, LR = 0.01, Slope = 2x.
# Run 10 iterations.

print(
    "\nTask 1: The 'Slow and Steady' Learner:- \n \t Start at x = 20, LR = 0.01, Slope = 2x. \n \t Run 10 iterations.\n\n")

x = 20
lr = 0.01

for _ in range(10):
    slope = 2 * x
    x = x - (slope * lr)

print(x)

# Task 2: The "Aggressive" Learner
# Start at x = 10, LR = 0.9, Slope = 2x.
# Why? This shows "Overshooting" - when the model is too aggressive and misses the target.

print(
    "\nTask 2: The 'Aggressive' Learner:- \n \t Watch the variable jump back and forth across the target. \n \t Why? This represents a model that is too unstable to find the best solution.\n\n")

x = 10
lr = 0.9

for _ in range(5):
    slope = 2 * x
    x = x - (slope * lr)
    print(x)

# Task 3: The "Constant Slope" Descent
# Start at x = 50, LR = 0.2, Slope = 5 (constant).
# Use a WHILE loop: while x > 0:
# Count how many steps it takes to reach the bottom.

print(
    "\nTask 3: The 'Constant Slope' Descent:- \n \t Use a while loop to count steps on a constant slope. \n \t Why? This teaches you how to stop an optimization process once a target is reached.\n\n")

x = 50
lr = 0.2
slope = 5
steps = 0

while x > 0:
    x = x - (slope * lr)
    steps += 1
print(f"{steps} steps it took to reach the bottom")

# Task 4: The Vanishing Gradient
# Start at x = 0.5, LR = 0.1, Slope = x**2.
# Why? This shows why learning stops when slopes are too small.

print(
    "\nTask 4: The Vanishing Gradient:- \n \t Observe how learning stalls when the slope is a small decimal. \n \t Why? This is a major hurdle in Deep Learning where weights stop updating.\n\n")

x = 0.5
lr = 0.1

for i in range(10):
    slope = x ** 2
    x = x - (slope * lr)
    print(f"Step {i}: x = {x:.2f}")

# Task 5: The "Momentum" Intuition (Rolling the Ball)
# Task: Update x using a 'change' variable that carries 90% of the previous step's speed.
# Formula: change = (0.9 * change) + (lr * slope) -> x = x - change
# Why? This simulates a ball picking up speed as it rolls down a hill, making learning more efficient.

print(
    "\nTask 5: The 'Momentum' Intuition:- \n \t Update x using a 'change' variable that carries speed from previous steps. \n \t Why? This is a key technique used in training large models like Neural Networks to speed up convergence.\n\n")

x = 0.5
lr = 0.1
change = 1

for i in range(10):
    slope = 2*x
    change = (0.9 * change) + (lr * slope)
    x = x - change
    print(f"Step {i}: x = {x:.4f} (Change/Speed: {change:.4f})")


# Task 6: Visualizing the "Zig-Zag" (Overfit/Instability)
# Task: Plot the gradient descent path with a very high Learning Rate (LR = 1.1).
# Why? This provides a visual warning of what happens when a model is too aggressive—it misses the target entirely.

print("\nTask 6: Visualizing the 'Zig-Zag':- \n \t Use Matplotlib to show how a high learning rate causes the optimizer to jump across the valley. \n \t Why? This visualizes 'Instability', which is a major part of High Variance in optimization.\n\n")

import numpy as np
import matplotlib.pyplot as plt

x_curve = np.linspace(-15, 15, 100)
y_curve = x_curve**2

x = 10
lr = 1.1
history_x = [x]
history_y = [x**2]

for i in range(10):
    slope = 2 * x
    x = x - (slope * lr)
    history_x.append(x)
    history_y.append(x**2)


plt.plot(x_curve,y_curve,color="gray")
plt.plot(history_x, history_y, "ro-")
plt.title("Learning Curve")
plt.show()

# Task 7: Finding the Minimum of a "Wide" Hill
# Task: Start at x = 10 and use a very gentle slope (0.5 * x).
# Why? This teaches you that the 'speed' of learning depends on both the Learning Rate AND the steepness of the data.

print("\nTask 7: Finding the Minimum of a 'Wide' Hill:- \n \t Observe the update speed when the hill is very flat. \n \t Why? This prepares you for 'Flat Loss Landscapes' where models struggle to find the exact bottom.\n\n")

x = np.linspace(-5,5,10)
lr = 0.01
history_x = [x]
history_y = [x**2]
for i in range(10):
    slope = 0.5*x
    x = x - (slope * lr)
    history_x.append(x)
    history_y.append(x**2)

plt.plot(x,x**2,color="gray")
plt.scatter(history_x,history_y,color="red")
plt.title("Task 7")
plt.show()
