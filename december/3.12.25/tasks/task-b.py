import os
import sys

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
file_path = os.path.join(script_directory,"assets","names.txt")

def add_names():
    with open(file_path, "a") as file:
        file.write(f"{input("Enter your name: ")}\n")

def display_names():
    with open(file_path, "r") as file:
        names = file.readlines()
        for name in names:
            print(name.strip().capitalize())

menu_dict = {
    ("(i)","i","1", "Add names"): add_names,
    ("(ii)","ii","2", "Display names"): display_names
}

menu = """
(i) Add names
(ii) Display names
"""

choice = input(f"{menu}\n>")
for option in menu_dict:
    if choice in option:
        menu_dict[option]()