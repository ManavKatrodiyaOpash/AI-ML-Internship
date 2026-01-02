str = input("Enter a sentence: ")

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
for letter in str:
    if letter in vowels:
        count += 1

print(f"There are {count} vowels in your sentence.")