def sum(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

if __name__ == "__main__":
    a = 10
    b = 5
    
    print("Sum:", sum(a,b))
    print("Subtract:", subtract(a,b))
    print("Multiply:", multiply(a,b))
    print("Divide:", divide(a,b))