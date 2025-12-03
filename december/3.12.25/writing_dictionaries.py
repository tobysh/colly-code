import os
import sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
file_path = os.path.join(script_directory,"etc","data.txt")

data = {"name": "Admore", "marks": [12, 14]}

with open(file_path, "w") as file:
    file.write(str(data))
print(f"Dictionary saved to {file_path}")