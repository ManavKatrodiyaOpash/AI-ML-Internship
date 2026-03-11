import re

chat1 = "hello my order number 54152563 is due please help"
chat2 = "my order # 48756985 is stuck do something to fix this"
chat3 = "your delivery guy is  making mistake with my order please do something order number 8745685214"

pattern = "order[^\d]*(\d*)"
print(re.findall(pattern, chat1))
print(re.findall(pattern, chat2))
print(re.findall(pattern, chat3))