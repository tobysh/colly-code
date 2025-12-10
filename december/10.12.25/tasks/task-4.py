from modules.get_file_path import get_path


while True:
    query = input("Enter a word to input: ").split(" ")
    if len(query) > 1:
        print("Only enter one word")
    else:
        break


