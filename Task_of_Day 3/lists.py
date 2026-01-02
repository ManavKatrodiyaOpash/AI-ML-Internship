# Given a list of integers, write a program to:
#       Remove duplicates
#       Sort the list in descending order

numbers = [1,2,3,3,4,5,5,6]
numbers = list(set(numbers))
numbers.sort(reverse=True)
print(numbers)

# Create a list of numbers from 1 to 50.
# Extract only the numbers divisible by 3 and 5.

num = [c for c in range(1,51)]
print(num)
ext_num = [c for c in num if c%3==0 and c%5==0]
print(ext_num)

# Given a list of strings, find:
# The longest string
# The shortest string

string_list = ["Hello", "How are you", "How's the work going"]
print(string_list)
print("The longest string in the list is :-",max(string_list, key=len))
print("The shortest string in the list is :-",min(string_list, key=len))