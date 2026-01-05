import os 
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
file_path = os.path.join(script_directory,"assets","numbers.txt")

numbers_sum = 0

with open(file_path, "r") as file:
    for line in file.readlines():
        if line.strip().isdigit():
            if int(line.strip()) % 2 == 0:
                numbers_sum += int(line.strip())

print(f"Sum of numbers: {numbers_sum}")