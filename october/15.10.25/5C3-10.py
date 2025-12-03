import random
secret = random.randint(1, 20)
guess = 0
while guess != secret:
    guess = int(input(f"Guess a number between 1 and 20: "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("You win! The number was " + str(secret))
