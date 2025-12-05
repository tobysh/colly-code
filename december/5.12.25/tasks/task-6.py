from modules.get_file_path import get_path

file_path = get_path("assets", "foods.txt")
print("Enter three of your favourite foods:")
with open(file_path, "w") as file:
    for i in range(3):
        file.write(input(f"({i}) >"))