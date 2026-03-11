import re

text = '''
Born	Elon Reeve Musk
June 28, 1971 (age 54)
Pretoria, South Africa
Citizenship	
South Africa
Canada (since 1988)
United States (since 2002)
Education  University of Pennsylvania (BA, BS)
Occupations	
CEO and product architect of Tesla
Founder, CEO, and chief engineer of SpaceX
Founder and CEO of xAI
Founder of the Boring Company and X Corp.
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
President of the Musk Foundation
Political party	Independent
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Children	14[a] (publicly known), including Vivian Wilson
Parents	
Errol Musk (father)
Maye Musk (mother)
Relatives	Musk family
Awards	Full list
'''

name_pattern = r"Born(.*)"
name = re.findall(name_pattern, text)

age_pattern = r"age (\d+)"
age = re.findall(age_pattern, text)

dob_pattern = r"Born.*\n(.*).\(age"
dob = re.findall(dob_pattern, text)

birth_place_pattern = r"\(age.*\n(.*)"
birth_place = re.findall(birth_place_pattern, text)

citizenship_pattern = r"Citizenship.*\n(.*)\n(.*)\n(.*)"
citizenship = re.findall(citizenship_pattern, text)

education_pattern = r"Education(.*)"
education = re.findall(education_pattern, text)

print(f"Name :- {name[0].strip()}")
print(f"Age :- {int(age[0])}")
print(f"DOB :- {dob[0]}")
print(f"Birth Place :- {birth_place[0]}")
print(f"Citizenship :- {citizenship[0]}")
print(f"Education :- {education[0].strip()}")