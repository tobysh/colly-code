from modules.get_file_path import get_path

file_path = get_path("assets", "foods.txt")
print("Enter three of your favourite foods:")
with open(file_path, "w") as file:
    for i in range(3):
        file.write(f"{input(f"({i+1}) >")}\n")

with open(file_path, "r") as file:
    print("Your favourite foods are:")
    for line in file.readlines():
        print(line.strip())