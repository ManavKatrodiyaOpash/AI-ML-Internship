# the game that printing nnumbers from 1 to desired number with the following rules
# for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz"
# for numbers which are multiples of both three and five print "FizzBuzz"

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    fizzbuzz(number)