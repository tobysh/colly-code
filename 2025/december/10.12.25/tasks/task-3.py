from modules.get_file_path import get_path

file_path = get_path(file_name="profile.txt")

num1 = None
while not num1:
    inp = input("Enter number 1 to be summed.\n>")
    try:
        num1 = int(inp)
    except ValueError:
        print("Enter a valid number.")

num2 = None
while not num2:
    inp = input("Enter number 1 to be summed.\n>")
    try:
        num2 = int(inp)
    except ValueError:
        print("Enter a valid number.")

result = num1+num2

string = f"The sum of {num1} and {num2} is {result}\n"

with open(file_path, "a") as file:
    file.write(string)