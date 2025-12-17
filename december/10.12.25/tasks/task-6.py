from modules.get_file_path import get_path

file_path = get_path(file_name="foods.txt")

with open(file_path, "r") as file:
    foods = file.readlines()

for i in range(len(foods)):
    foods[i] = foods[i].strip()
foods.sort()
print(foods)