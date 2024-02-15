import json
from pprint import pprint

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)

# ดึงข้อมูล attribute ของ object
person_vars = vars(person)

# แปลงข้อมูลให้อยู่ในรูปแบบของ string
# person_vars_str =   # หรือ pprint(person_vars)

# # แสดงผลลัพธ์
# print(json.dumps(person_vars, indent=4))

pprint(person_vars)