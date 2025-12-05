from modules.get_file_path import get_path

file_path = get_path("assets", "grades.csv")

header = "Name,Grade"
entries = []

with open(files)
for i in range(3):
    name = input("Enter a name: ").strip().capitalize()
    grade = -1
    while grade == -1:
        buffer = input("Enter the number grade: ").strip()
        try:
            grade = int(buffer)
        except ValueError:
            print("Enter a valid number: ")
    entry = f"{name},{grade}"
