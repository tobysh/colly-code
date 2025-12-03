balance = 0

def show_menu():
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

running = True
while running:
    show_menu()
    option = input("Choose option: ")
    
    if option == "1":
        print("Current balance: £" + str(balance))
    elif option == "2":
        amount = int(input("Deposit amount: "))
        balance += amount
        print("You deposited £" + str(amount))
    elif option == "3":
        withdraw = int(input("Withdraw amount: "))
        if withdraw > balance:
            print("Insufficient balance")
        else:
            balance = balance - withdraw
            print(f"You withdrew: £{withdraw}")
    elif option == "4":
        running = False
    elif option > "4":
        print("Invalid option")
