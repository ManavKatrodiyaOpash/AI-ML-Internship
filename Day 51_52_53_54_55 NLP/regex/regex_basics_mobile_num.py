import re

chat1 = "hello my number is 1234567890. whats yours ??"
chat2 = "hello my number is (123)-456-7890."
chat3 = "hello here is mine, 1223334444"

pattern = "\d{10}|\(\d{3}\)-\d{3}-\d{4}"
print(re.findall(pattern, chat1))
print(re.findall(pattern, chat2))
print(re.findall(pattern, chat3))