import random

numbers = []

for i in range(5):
    numbers.append(random.randint(1,20))
found = False
unfound_numbers = numbers.copy()
while not found:
    validGuess = False
    while not validGuess:
        guess = int(input("Guess a number from 1 to 20: "))
        if guess >= 1 and guess < 21:
            validGuess = True
    if guess in unfound_numbers:
        print(guess, "is in the list!")
        unfound_numbers.remove(guess)
        if len(unfound_numbers) == 0:
            found = True
    else:
        print(guess, "isn't in the list!")

print("You win")
print(numbers)