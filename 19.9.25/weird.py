import random
import string
import os
import time
phrase = "This is a string"
progress = ""
all = string.ascii_letters+string.punctuation+string.digits + " "
for i in range(len(phrase)):
    
    letter = ""
    while letter != phrase[i]:
        print(progress, end="")
        os.system('clear')
        letter=random.choice(all)
        print(letter)
        time.sleep(0.05)
    progress += letter