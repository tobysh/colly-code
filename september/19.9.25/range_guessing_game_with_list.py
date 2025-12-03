import random
import os

lower = int(input("Enter your lower bound for the guessing game: "))
upper = int(input("Enter your upper bound for the guessing game: "))

while lower > upper:
    print("Lower cannot be higher than upper.")
    lower = int(input("Enter your lower bound for the guessing game: "))
    upper = int(input("Enter your upper bound for the guessing game: "))

num = random.randint(lower,upper)

guess_list = []
guessed = False
guesses = 0
while not guessed:
    guess = int(input(f"({guesses+1}) Pick a number between {lower} and {upper}: "))
    guesses += 1
    guess_list.append(guess)
    if (guess % 2 == 0) and (abs(num - guess) < 10):
        print("So close!")
    if (guess % 2 != 0) and (abs(num - guess) > 30):
        print("Way off!")
    os.system('clear')
    if guess == num:
        guessed = True
        print(f"Correct! You guessed {num} in {guesses} guesses!")
        print(f"Your guesses: {guess_list}")
    elif num > guess:
        print("Too low!")
    elif num < guess:
        print("Too high!")
