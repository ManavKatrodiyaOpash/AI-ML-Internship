# Given a tuple of integers:
#       Find the maximum and minimum values
#       Convert the tuple into a list and remove all even numbers

tup = (1, 2, 5, 8, 45, 67, 23, 88, 90, 76, 54, 322, 567, 876, 544)
print(tup)
print("the maximum value of the given tuple is :-", max(tup))
print("the minimum value of the given tuple is :-", min(tup))

tup = list(tup)
print(tup)
tup = [c for c in tup if c % 2 != 0]
print(tup)

# Create a tuple containing mixed data types.
# Count how many elements are strings.

tupp = (1,45,768,342,23,34,"hello", "how are you","how's the work going",67,89,90,"Fine")
print(tupp)
count = 0
for i in tupp:
    if type(i) == str:
        count += 1
print(f"The count of string in the tuple is :- {count}")