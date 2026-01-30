global balance
balance = 500

def check_balance():
    print(balance)
    
def deposit_money():
    global balance 
    addition = None
    while not addition:
        try:
            addition = (round(float(input("How much are you depositing?\n> £")), 2))
        except ValueError:
            print("Invalid amount")
    if balance > 0:
        balance += addition
        print(f"Successfuly deposited £{addition}")
    else:
        print("Deposit amounts cannot be below 0.")
    
def withdraw_money():
    global balance 
    amount = None
    while not amount:
        try:
            amount = (round(float(input("How much are you withdrawing?\n> £")), 2))
        except ValueError:
            print("Invalid amount")
    if balance > 0:
        if balance < amount:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"Successfuly withdrew £{amount}")
    else:
        print("Withdraw amounts cannot be below 0.")
        

menu = """
--- Bank app -----------------
    (1) Check balance
    (2) Deposit money
    (3) Withdraw money
    (4) Exit
------------------------------
"""

menu_dict = {
    1: check_balance,
    2: deposit_money,
    3: withdraw_money,
    4: exit
}

while True:
    print(menu)

    choice = None
    while not choice:
        try:
            choice = int(input(">"))
        except ValueError:
            print("Invalid choice")
    menu_dict[choice]()