from modules.get_file_path import get_path

file_path = get_path("assets", "story.txt")

with open(file_path, "r") as file:
    story = file.read()

el = input("Enter a single word to search for: ").strip().split(" ")[0]

count = 0
for word in story.split(" "):
    if word == el:
        count += 1

print(f"The word {el} appears {count} times in the story")