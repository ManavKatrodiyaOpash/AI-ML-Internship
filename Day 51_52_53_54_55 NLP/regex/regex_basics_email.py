import re

chat1 = "hello my gmail is abc@xyz.com whats yours ??"
chat2 = "hello mine is abXY_45hello@abcd.com"
chat3 = "mine is manav@gmail.com"

pattern = "[a-z0-9A-Z_]*@[a-z0-9A-Z]*\.com"

print(re.findall(pattern, chat1))
print(re.findall(pattern, chat2))
print(re.findall(pattern, chat3))