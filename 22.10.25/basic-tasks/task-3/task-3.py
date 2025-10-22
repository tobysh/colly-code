from cryptography.fernet import Fernet
import os
if os.path.isfile("/workspaces/colly-code/22.10.25/basic-tasks/task-3/key.key"):
    with open("/workspaces/colly-code/22.10.25/basic-tasks/task-3/key.key", "rb") as file:
        key = file.read()
else:
    key = Fernet.generate_key()
    with open("/workspaces/colly-code/22.10.25/basic-tasks/task-3/key.key", "wb") as file:
        file.write(key)

f = Fernet(key)

if os.path.isfile("/workspaces/colly-code/22.10.25/basic-tasks/task-3/encrypted-word.txt"):
    with open("/workspaces/colly-code/22.10.25/basic-tasks/task-3/encrypted-word.txt", "r") as file:
        encrypted_word = file.read()
        word = (f.decrypt(encrypted_word)).decode()
        
else:
    with open("/workspaces/colly-code/22.10.25/basic-tasks/task-3/encrypted-word.txt", "wb") as file:
        word = input("No word defined, enter a word: ")
        token = f.encrypt(word.encode())
        file.write(token)

guess = input("Guess the word!\n>").lower()
if guess == word.lower():
    print("Correct! The word is", word)