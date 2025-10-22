messages = {
    "coffee":"Here\'s your coffee!",
    "tea":"Tea coming right up!",
    "hot chocolate":"Hot chocolate ready!"
}

choice = input("What drink would you like?\nTea\nHot chocolate\nCoffee\n>").lower().strip()
if messages.get(choice) != None:
    print(messages.get(choice))
else:
    print("Sorry, we don\'t serve that.")