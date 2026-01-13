# Given a list of dictionaries representing employees:
#     Increase each employee’s salary by 10%
#     Store the result in a new list
emp = [
  {"name": "Alice",
   "salary": 50000},
  {"name": "Bob",
   "salary": 60000},
  {"name": "Charlie",
   "salary": 55000}
]
# print(emp)
# print(emp[0]["name"])
# print(emp[0]["salary"])
print(type(emp))
print(type(emp[0]))

new_dict = [{}]
for i in range(len(emp)):
    emp[i]["salary"] = emp[i]["salary"] + int(emp[i]["salary"]*(10/100))
    # new_dict.append(emp[i]["name"], emp[i]["salary"])
print(emp)

# Given a list of numbers:
# Replace all negative numbers with 0
# Keep positive numbers unchanged
import random
lst = [random.randint(-100, 100) for _ in range(20)]
print(lst)
lst = [c if c>0 else 0 for c in lst]
print(lst)


# Given a list of sentences:
# Create a list of unique words (case-insensitive)
sentences = ["How are you","this is a test"]
words = [word.lower() for word in sentences for word in word.split()]
uniqueWords = list(set(words))
print(uniqueWords)



# You have a list of dictionaries representing employees:
# Task:
#     Increase the salary of employees in the IT department by 10%
#     Keep HR salaries unchanged
#     Store the result in a new list of dictionaries

employees = [
    {"name": "Alice", "salary": 50000, "department": "IT"},
    {"name": "Bob", "salary": 60000, "department": "HR"},
    {"name": "Charlie", "salary": 55000, "department": "IT"},
    {"name": "David", "salary": 70000, "department": "HR"}
]
print(employees)
for i in range(len(employees)):
    if employees[i]["department"] != "HR":
        employees[i]["salary"] = employees[i]["salary"] + int(employees[i]["salary"]*(10/100))
print(employees)


# Random List Filtering & Transformation
#     Generate a list of 30 random integers between -50 and 50
#     Remove all negative numbers
#     Multiply all remaining numbers divisible by 5 by 2
#     Print the final list

lst_num = [random.randint(-50,50) for _ in range(30)]
print(lst_num)
lst_pos_num = [c for c in lst_num if c > 0]
print(lst_pos_num)
filter_num = [c*2 for c in list(filter(lambda x: x%5==0, lst_pos_num))]
print(filter_num)