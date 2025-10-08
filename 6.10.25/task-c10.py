items = ["Beans", "Bananas"]

def addDivider():
    print("\n-------\n")

def addItem():
    items.append(input("Enter the item you'd like to add: ").capitalize())


def removeItem():
    try:
        print(f"Removing {items.pop(int(input('Enter the number of the item you\'d like to remove: ')))}...")
    except IndexError:
        print("Not a valid number")
    except ValueError:
        print("Not a number, please enter the number next to the item you'd like to remove.")
def exitProgram():
    exit()

def showItems():
    print("Items:")
    for i in range(len(items)):
            print(f"({i}) {items[i]}")

optionMap = {
    '1':addItem,
    '2':removeItem,
    '3':exitProgram
}



while True:
    showItems()
    options = """
Choose a number corresponding to the option
(1) Add an item
(2) Remove an item
(3) Exit
    """
    addDivider()
    print(options)
    option = (input(">"))
    try:
        optionMap[option]()
    except KeyError:
        print("Entry was not a valid option")
