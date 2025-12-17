from modules.get_file_path import get_path
import json

file_path = get_path(file_name="student.txt")

student={
    "name":"Ali",
    "age":18,
    "grade":"A"
}
with open(file_path, "w") as file:
    for item in student.items():
        file.write(f"{item[0]}: {item[1]}\n")

