import random

numbers = []
hidden_numbers = ["X","X","X","X","X"]
entries = []

for i in range(5):
    numbers.append(random.randint(1,20))

for i in range(5):
    validGuess = False
    while not validGuess:
        guess = int(input("Guess a number from 1 to 20: "))
        if guess >= 1 and guess < 21:
            validGuess = True
        else:
            print("Guess out of range, try again.")
    entries.append(guess)

for i in range(len(numbers)):
    if numbers[i] == entries[i]:
        hidden_numbers[i] = numbers[i]

    
