from modules.get_file_path import get_path
file_path = get_path(file_name="foods.txt")

foods=[]
for i in range(5):
    foods.append(input(f"({i}) Enter one of your favourite foods: "))

with open(file_path, "w") as file:
    for food in foods:
        file.write(food+"\n")

