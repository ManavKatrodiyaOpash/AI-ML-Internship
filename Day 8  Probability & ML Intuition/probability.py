import numpy as np
import random


# Task 1: Basic Probability Logic
# Task: Create a function `calc_probability` that takes 'favorable_outcomes' and 'total_outcomes'.
# The function must return the probability as a decimal and a percentage.
# Why? This is the foundation of every classification algorithm. Before a model predicts, it calculates these ratios.

print("\nTask 1: Basic Probability Logic:- \n \t Create a function to calculate decimal and percentage probability. \n \t Why? Every ML prediction (like Spam vs Not Spam) starts as a simple ratio of occurrences.\n\n")

def calc_probability(favourable_outcomes, total_outcomes):
    probability = favourable_outcomes / total_outcomes
    prob_percentage = probability*100

    return probability, prob_percentage

target_outcomes = 36
total_outcomes = 108
prob,prob_percen = calc_probability(target_outcomes, total_outcomes)
print(f"The probability is :- {prob:.2f}")
print(f"The probability percentage is :- {prob_percen:.2f}%")


# Task 2: Independent Events Simulation
# Task: Simulate flipping two coins at the same time 5,000 times.
# Calculate the probability of getting "Double Heads" (Heads on Coin A AND Heads on Coin B).
# Why? Understanding independent events helps you understand how models handle multiple features at once.

print("\nTask 2: Independent Events Simulation:- \n \t Simulate 5,000 double coin flips to find the probability of Double Heads. \n \t Why? In ML, we often assume features are independent to simplify complex calculations (Naive Bayes intuition).\n\n")


def coin_flip(count,options):
    num = 0

    for _ in range(count):
        coin_a = random.choice(options)
        coin_b = random.choice(options)
        if coin_a == "Heads" and coin_b == "Heads":
            num += 1

    return num/count

options = ["Heads", "Tails"]
count = 5000

prob = coin_flip(count,options)
print(f"The probability of getting 'Double Heads' is :- {prob:.2f}")


# Task 3: Conditional Probability Filter
# Task: Create a list of 20 numbers (1 to 20).
# Calculate the probability that a number is "Greater than 15" GIVEN that it is an "Even Number".
# Why? Conditional probability is the "filtering" power of Machine Learning. It allows models to narrow down possibilities.

print("\nTask 3: Conditional Probability Filter:- \n \t Find P(Number > 15 | Number is Even) using a list of 1-20. \n \t Why? Real-world data is conditional; a model needs to know the probability of a result based on a specific attribute.\n\n")

lst = [c for c in range(1,21)]
print(lst)

p_a = [c for c in lst if c>15]
print(p_a)
p_b = [c for c in lst if c%2==0]
print(p_b)
a_intersec_b = np.intersect1d(p_a,p_b)
print(a_intersec_b)

prob_p_a = len(p_a) / len(lst)
prob_p_b = len(p_b) / len(lst)
prob_a_intersec_b = len(a_intersec_b) / len(lst)

prob = prob_a_intersec_b / prob_p_b

print("P(A/B) = P(A ∩ B) / P(B)")
print(f"P(Number > 15 | Number is Even) = {prob:.2f}")


# Task 4: The Law of Large Numbers (Stability Test)
# Task: Simulate a random "Success" (True/False) with a 30% chance.
# Run this simulation for 10 iterations, then 1,000, then 100,000.
# Print the results for all three to see how close they get to 30%.
# Why? This proves why "Small Data" can be misleading and why "Big Data" provides the mathematical truth.

print("\nTask 4: The Law of Large Numbers (Stability Test):- \n \t Compare a 30% success rate across three different sample sizes. \n \t Why? This helps you understand 'Variance'—small samples fluctuate wildly, while large samples provide stability.\n\n")

def run_simulation(num):
    sucess_count = 0
    for _ in range(num):
        sim = random.random()
        if sim < 0.3:
            sucess_count += 1
    prob = (sucess_count / num)*100
    return prob

print(f"Result with 10 iteration :- {run_simulation(10)}")
print(f"Result with 1000 iteration :- {run_simulation(1000):.3f}")
print(f"Result with 100000 iteration :- {run_simulation(100000):.3f}")

# Task 5: Frequency Distribution (The Histogram Logic)
# Task: Generate 1,000 random integers between 1 and 10.
# Count how many times each number appears and print the "Probability Distribution" (Count / Total).
# Why? This is how models see data. Before learning, they look at the distribution of values to understand the "Shape" of the data.

print("\nTask 5: Frequency Distribution (The Histogram Logic):- \n \t Map out the probability of every possible outcome in a 1-10 range over 1,000 trials. \n \t Why? Understanding distributions is key to identifying 'Outliers' and 'Normal' patterns in a dataset.\n\n")

lst = np.random.randint(1,11,1000)
count = {i:0 for i in range(1,11)}

for value in lst:
    count[value] += 1

print(count)

for i in range(1,11):
    prob = count[i]/len(lst)

    print(f"Probability of occuring {i} in list is :- {prob:.2f}")