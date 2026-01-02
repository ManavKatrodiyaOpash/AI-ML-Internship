try:
    with open("text.txt","r") as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("File Not Found")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

try:
    print("Division of two number is :-",num1/num2)

except ZeroDivisionError:
    print("Division by zero error")

# try, exception, else and finally :- \
try:
    print("this will try to run")
except:
    print("this will run if error occurs in try")
else:
    print("this will run if no error occurs in try")
finally:
    print("this will run no matter what")