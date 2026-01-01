num = int(input("Enter a number: "))

def fact(num):
    for i in range(1, num + 1):
        if num == 1 or num == 0:
            return 1
        else:
            return num * fact(num - 1)

print(f"Factorial of {num} is {fact(num)}")