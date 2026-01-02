# Lambda function is used to do one-liner function

def square(n):
    return n ** 2


print(square(5))

# Instead we can use lambda
# lambda arguments: expression
square = lambda x: x ** 2
print(square(5))

# map() Function :-
# map(function, iterable)
# apply every item in iterable
lst = [1, 2, 3, 4, 5]
square = list(map(lambda x: x ** 2, lst))
print(square)

# filter() Function :-
# filter(function, iterable)
# apply on a condition
lst = [1, 2, 3, 4, 5]
filter = list(filter(lambda x: x % 2==0, lst))
print(filter)

# all() Function :-
lst = [2, 4, 6, 8]
result = all(x % 2 == 0 for x in lst)  # True if all numbers are even
print(result)  # Output: True


# any() Function :-
lst = [1, 3, 4, 5]
result = any(x % 2 == 0 for x in lst)  # True if any number is even
print(result)  # Output: True
