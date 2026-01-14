import random


outcomes=["Heads", "Tails"]

headsOrTails = random.choice(outcomes)

userChoice = input("Heads or tails?\n>").capitalize()

if userChoice == headsOrTails:
    print(f"Correct! The outcome was {headsOrTails.lower()}!")
else:
    print(f"Wrong! The outcome was {headsOrTails.lower()}.")