from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'Manav Katrodiya', 'age':'21'}

print(new_person)