import os
from modules.get_file_path import get_path
file_path = get_path("assets", "guestbook.txt")

name = input("Enter your name: ").capitalize()
comment = input("Enter a comment regarding the event: ")

entry = f"Name: {name}, Comment: {comment}\n"

entry_type = "w"
if os.path.exists(file_path):
    entry_type = "a"

with open(file_path, entry_type) as file:
    file.write(entry)

print("Guestbook entries:")
with open(file_path, "r") as file:
    for line in file.readlines():
        print(line.strip())