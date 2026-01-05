import os
import sys

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
file_path = os.path.join(script_directory,"assets","numbers.txt")
avg_path = os.path.join(script_directory,"assets","average.txt")

def enter_numbers():
    while True:
        try:
            num = int(input("Enter a number (-1 to exit the loop): "))
            if num == -1:
                break
            with open(file_path, "a") as file:
                file.write(f"{num}\n")
        except ValueError:
            print("Enter a valid number")
        except FileNotFoundError:
            print("File not found")
            print("Creating file...")
            open(file_path, "w").close()

def summarise():
    with open(file_path, "r") as file:
        numbers = file.readlines()
        for num in numbers:
            print(num.strip(), end=", ")
        print()
        nums = [int(n.strip()) for n in numbers]
        average = sum(nums)/len(nums)
        print(average)
    with open(avg_path, "w") as file:
        file.write(str(average))
        
        

menu_dict = {
    ("(i)","i","1", "Enter numbers"): enter_numbers,
    ("(ii)","ii","2", "Summarise"): summarise
}

menu = """
(i) Enter numbers
(ii) Summarise
"""

choice = input(f"{menu}\n>")
for option in menu_dict:
    if choice in option:
        menu_dict[option]()