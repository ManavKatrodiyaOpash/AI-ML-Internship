import numpy as np
import random

from gradiant import learning_rate

# Task 1: The Bias-Variance Gap (Underfit vs. Overfit)
# Task: Define the training and testing error for two fictional models.
# Calculate the 'Gap' (Test Error - Train Error) and print which model is 'Overfitting'.
# Why? A small gap means the model is stable. A huge gap means the model is too sensitive (High Variance).

print("\nTask 1: The Bias-Variance Gap:- \n \t Compare a 'Simple' model vs a 'Complex' model. \n \t Calculate the error gap to identify Overfitting. \n \t Why? This is how Data Scientists diagnose if a model is memorizing data instead of learning patterns.\n\n")

# Model A (Underfit/High Bias): High error on both
train_err_a = 0.28
test_err_a = 0.30

# Model B (Overfit/High Variance): Low train error, but high test error
train_err_b = 0.02
test_err_b = 0.38

print("For Model-A :- ")
print("\ttrain error is :- ",train_err_a)
print("\ttest error is :- ",test_err_a)
gap_a = test_err_a - train_err_a
print(f"\tGap is :- {gap_a:.2f}")

if gap_a < 0.2:
    print(f"Model-A is Underfitting")
else:
    print(f"Model-A is Overfitting")

print("For Model B :- ")
print("\ttrain error is :- ",train_err_b)
print("\ttest error is :- ",test_err_b)
gap_b = test_err_b - train_err_b
print("\tGap is :- ",gap_b)

if gap_b < 0.2:
    print(f"Model-B is Underfitting")
else:
    print(f"Model-B is Overfitting")
# Logic: Calculate the gaps and use an IF statement to print which is overfitting.


# Task 2: Simulating "Noisy" Data (Real World Variance)
# Task: Create a list of 50 values that should all be '10'.
# Add random noise to each value using random.uniform(-2, 2).
# Calculate the Standard Deviation of the result.
# Why? Variance in a model often comes from high variance (noise) in the raw data.

print("\nTask 2: Simulating 'Noisy' Data:- \n \t Add random fluctuations to a dataset and measure the standard deviation. \n \t Why? This helps you understand how 'unstable' data impacts the reliability of your model.\n\n")

lst = np.array([10 for _ in range(50)])
print(lst)
print(np.mean(lst))
print(np.std(lst))

for i in range(len(lst)):
    lst[i] = lst[i] + random.uniform(-2,2)
print(lst)
print(np.mean(lst))
print(np.std(lst))


# Task 3: Manual Gradient Descent Step
# Task: You are at position x = 5. The slope is calculated as (2 * x).
# Take 10 steps using a learning_rate of 0.1. Update x each time: x = x - (LR * slope).
# Print the value of x at each step to see it "descend" to 0.
# Why? This is the "Optimization" process that solves the Bias-Variance problem by finding the best fit.

print("\nTask 3: Manual Gradient Descent Step:- \n \t Perform 10 manual updates to a weight variable. \n \t Why? Understanding the update rule is key to knowing how models like Neural Networks actually learn.\n\n")

x = 5
learning_rate = 0.1


for _ in range(10):
    slop = 2 * x
    x = x - (learning_rate * slop)
print(x)

# Task 4: The "Biased" Dataset (Model Bias)
# Task: Create a 90/10 imbalanced dataset and calculate "Lazy Accuracy".
# Why? High Bias can hide inside high accuracy numbers if your data is imbalanced.

print("\nTask 4: The 'Biased' Dataset:- \n \t Create a 90/10 imbalanced dataset and calculate accuracy for a model that always predicts '0'. \n \t Why? This shows how a 'Lazy' model with High Bias can appear successful but fail to find the minority pattern.\n\n")

# Step 1: Create 1000 samples where 900 are '0' and 100 are '1'
# Step 2: Calculate accuracy if we predicted '0' for everything

zeros = np.zeros(900)
ones = np.ones(100)

dataset = np.concatenate([zeros, ones])
predictions = np.zeros(1000)

correct_predictions = np.sum(predictions == dataset)
accuracy = (correct_predictions / len(dataset)) * 100

print(correct_predictions)
print(accuracy)

print(f"Total Patients: {len(dataset)}")
print(f"Actual Sick Patients: {int(np.sum(dataset))}")
print(f"Model Accuracy: {accuracy:.2f}%")

if accuracy >= 90:
    print("CRITICAL LESSON: The model has 90% accuracy but 0% ability to find sick people.")
    print("This is the 'Accuracy Paradox' of High Bias models.")


# Task 5: Standard Deviation from Scratch
# Task: Manually calculate the Standard Deviation of [2, 4, 4, 4, 5, 5, 7, 9].
# Why? Knowing the internal math of Variance helps you understand how models penalize 'outliers' or 'noise'.

print("\nTask 5: Standard Deviation from Scratch:- \n \t Manually calculate Mean, Variance, and SD for a small dataset. \n \t Why? This removes the 'magic' from the code and shows exactly how we quantify data spread.\n\n")

data = [2, 4, 4, 4, 5, 5, 7, 9]

# Step 1: Calculate Mean
# Step 2: Calculate Variance (Mean of squared differences)
# Step 3: Calculate Standard Deviation (Square root of Variance)

print(f"Mean is :- {np.mean(data)}")
print(f"Variance is :- {np.var(data)}")
print(f"Standard Deviation is :- {np.std(data)}")