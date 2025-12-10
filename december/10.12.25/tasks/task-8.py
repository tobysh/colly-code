from modules.get_file_path import get_path
import json

file_path = get_path(file_name="student.json")

student={
    "name":"Ali",
    "age":18,
    "grade":"A"
}

for item in student.items():
    print(item)

