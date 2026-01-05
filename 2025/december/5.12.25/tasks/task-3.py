import os 
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
file_path = os.path.join(script_directory,"assets","numbers.txt")

numbers = 0

with open(file_path, "r") as file:
    for line in file.readlines():
        if line.strip().isdigit():
            numbers += 1

print(f"There are {numbers} numbers in the file")    