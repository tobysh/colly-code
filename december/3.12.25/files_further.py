import sys
import os
import json

data = {
"name": "Admore",
"role": "Lecturer",
"location": "Salisbury"
}

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
file_path = os.path.join(script_directory,"etc","data.json")

with open(file_path, "w") as file:
    json.dump(data, file)