from modules.get_file_path import get_path

file_path = get_path("assets","profile.txt")

name = input("What\'s your name?\n>").strip().capitalize()

age = None
while not age:
    inp = input("How old are you?\n>")
    try:
        age = int(inp)
    except ValueError:
        print("Enter a valid number.")

with open(file_path, "w") as file:
    file.write(f"My name is {name} and I\'m {age} years old\n")