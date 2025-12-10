from modules.get_file_path import get_path

file_path = get_path(file_name="story.txt")

while True:
    query = input("Enter a word to input: ").split(" ")
    if len(query) > 1:
        print("Only enter one word")
    else:
        query = (query[0])
        break

with open(file_path, "r") as file:
    words = file.read().split(" ")
    count = 0
    for word in words:
        if word == query:
            count+=1

print(f"The word {query} appears {count} times in the file.")
