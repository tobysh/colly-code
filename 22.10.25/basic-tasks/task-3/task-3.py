from cryptography.fernet import Fernet
import os

TEXT_FILE = "/workspaces/colly-code/22.10.25/basic-tasks/task-3/encrypted-word.txt"
KEY_FILE = "/workspaces/colly-code/22.10.25/basic-tasks/task-3/key.key"

if os.path.isfile(KEY_FILE):
    with open(KEY_FILE, "rb") as file:
        key = file.read()
else:
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as file:
        file.write(key)

f = Fernet(key)

if os.path.isfile(TEXT_FILE):
    with open(TEXT_FILE, "r") as file:
        encrypted_word = file.read()
        word = (f.decrypt(encrypted_word)).decode()
        
else:
    with open(TEXT_FILE, "wb") as file:
        word = input("No word defined, enter a word: ")
        token = f.encrypt(word.encode())
        file.write(token)

while True:
    guess = input("Guess the word!\n>").lower()
    if guess == word.lower():
        print("Correct! The word is", word)
        break
    else:
        print("Incorrect! Guess again or delete the encrypted-word.txt file to reset it.")