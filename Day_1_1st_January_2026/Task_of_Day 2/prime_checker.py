num = int(input("Enter a number: "))

def prime_checker(num):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count += 1
            
    if count == 2:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    prime_checker(num)