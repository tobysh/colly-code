from modules.get_file_path import get_path
import random

file_path = get_path("assets", "quiz.txt")

nums = []

for i in range(5):
    nums.append(random.randint(0,20))

with open(file_path, "w") as file:
    for num in nums:
        file.write(f"{num}\n")

possible_answers = []

with open (file_path, "r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        possible_answers.append(int(lines[i].strip()))



guessed = False
while not guessed:
    guess = None
    while guess == None:
        inp = input("Enter a number between 0 and 20: ")
        try:
            guess = int(inp)
            if guess > 20 or guess < 0:
                guess = None
        except ValueError:
            pass
    if guess in possible_answers:
        guessed = True
        print("Congrats!")
    else:
        print("Incorrect")
print("Possible guesses: ")
for line in lines:
    print(line.strip())