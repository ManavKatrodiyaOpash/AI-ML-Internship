# Use a lambda function to:
# Find the square of a number

lst=[1, 2, 3, 4, 5]
square = lambda x: x ** 2
squared_lst = list(map(square, lst))
print("Squared List:", squared_lst)


# Sort a list of tuples (name, age) based on:
# Age using a lambda function

people = [("Manav",21), ("Bob",20),("C",17),("D",26),("E",10)]
sorted_people = sorted(people,key=lambda x: x[1])
print(sorted_people)

# Use filter() with a lambda to:
# Extract all prime numbers from a given list

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))
prime_num = list(filter(prime,num))
print(prime_num)

# Square of even numbers only
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
square = map(lambda x:x**2,filter(lambda x:x%2==0,lst))
square_num = list(square)
print(square_num)

# check if all numbers are positive :-
lst = [1,2,3,-4,5]
check = all(x>0  for x in lst)
print(check)

check_neg = any(x<0 for x in lst)
print(check_neg)

# check if all numbers are divisible by 5 or not
lst = [5,10,15,20,25]
check_div = all(lambda x:x%5==0 for x in lst)
print(check_div)

# Find all squared numbers from 1 to 50
lst = [c for c in range(1,51)]
print(lst)
check_squared = list(filter(lambda x:(x**0.5).is_integer(),lst))
print(check_squared)
