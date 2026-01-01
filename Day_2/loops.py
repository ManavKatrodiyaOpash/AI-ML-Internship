# While-loop, for-loop, do-while loop in Python

# Example of while loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# Example of for loop
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print("Number is:", num)

# Example of do-while loop using while loop
num = 1


while True:
    print(f"Yes, your number {num} is less than 10")
    num += 1
    
    if not (num <= 10):
        break
# there is no do-while loop in directly on Python to mimic do-while loop we can use this trick written above