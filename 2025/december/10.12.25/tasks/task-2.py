from modules.get_file_path import get_path

file_path = get_path("assets", "profile.txt")

with open(file_path, "r") as file:
    print(file.read().upper())