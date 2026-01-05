import os 
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
file_path = os.path.join(script_directory,"assets","greetings.txt")

with open(file_path, "r") as file:
    for line in file.readlines():
        print(line)