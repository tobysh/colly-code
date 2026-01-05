from modules.get_file_path import get_path

file_path = get_path("assets", "grades.csv")

header = "Name,Grade\n"
entries = []

with open(file_path, "w") as file:
    file.write(header)
    for i in range(3):
        name = input("Enter a name: ").strip().capitalize()
        grade = -1
        while grade == -1:
            buffer = input("Enter the number grade: ").strip()
            try:
                grade = int(buffer)
            except ValueError:
                print("Enter a valid number: ")
        entry = f"{name},{grade}\n"
        file.write(entry)

with open(file_path, "r") as file:
    for line in file.readlines():
        print(line.strip())