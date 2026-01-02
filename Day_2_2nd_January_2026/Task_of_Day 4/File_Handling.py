# Create a list in Python
# Write each item from this list into a new file called tools.txt, with each item on a new line.
# Read the file back and store the lines into a new Python list.
import csv

tools = ["Python", "VS Code", "VirtualEnv", "Pip"]

with open("tools.txt","w") as f:
    for word in tools:
        f.write(word+"\n")


# Create a file called grades.csv with the content:
# Write a script to read this file, skip the header line, and calculate the average score.
# Bonus: Print only the names of students who scored above 80.

with open("grades.csv","r") as f:
    reader = csv.reader(f)
    header = next(reader)  # This skips the "Name,Score" header row
    scores = []
    print("Here are the student name who scores more than 80 marks")
    for row in reader:
        name =row[0]
        score = int(row[1])

        if score >= 80:
            print(name)

        scores.append(score)


    print(f"Average score is :- {sum(scores)/len(scores):.2f}")


# Imagine you have a log file and you need to find how many times an error occurred.
# Create a file server.log and paste several lines of text, some containing the word "ERROR" and some containing "INFO".
# Write a script that reads the file and counts how many times the word "ERROR" appears.
# Write the final count into a new file called report.txt.Imagine you have a log file and you need to find how many times an error occurred.
# Create a file server.log and paste several lines of text, some containing the word "ERROR" and some containing "INFO".
# Write a script that reads the file and counts how many times the word "ERROR" appears.
# Write the final count into a new file called report.txt.

with open("server.log","r") as f:
    content = f.readlines()
    error_count = 0
    info_count = 0

    for line in content:
        if line.startswith("error"):
            error_count += 1
        elif line.startswith("info"):
            info_count += 1

    print(f"There are {error_count} errors and {info_count} infos")



# Create three text files: data1.txt, data2.txt, and data3.txt, each with a random number inside.
# Write a script that:
# Uses a list of filenames files = ["data1.txt", "data2.txt", "data3.txt"].
# Loops through the list.
# Reads the number from each.
# Prints the sum of all numbers.
# Use a try-except block inside the loop just in case one file is missing.

files = ["data1.txt", "data2.txt", "data3.txt"]
count = 0

for file in files:
    try:
        with open(file,"r") as f:
            content = f.read()
            content = int(content)
            count += content
        print(f"There is the sum of numbers in files :- {count} ")

    except FileNotFoundError:
        print(f"File '{file}' not found")