import os
import sys

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
file_path = os.path.join(script_directory,"assets","name.txt")


name = input("Enter your name: ")
with open(file_path, "w") as file:
    file.write(name)

with open(file_path, "r") as file:
    print(f"Hello {file.read()}")
