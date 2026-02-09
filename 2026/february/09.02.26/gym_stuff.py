from datetime import datetime

types = {
    "basic": 19.99,
    "plus": 24.99,
    "premium": 29.99
}

members = {}

payments = {}

def register():
    name = input("Enter your name: ").capitalize()
    age = None
    while not age:
        try:
            age = int(input("Enter your age\n>"))
        except ValueError:
            print("Invalid age")
    id = (len(members)+1)
    members.update({
        id:
            {"name": name,
             "age": age,
             "membership":None}
            })
    print(f"Done! Your ID is {id}")
    
def view_types():
    for tier in types.items():
        print(f"{tier[0].capitalize()}: {tier[1]}")
    
def calculate_fee():
    while True:
        tier = input("Enter your membership: ").lower()
        level = types.get(tier)
        if types.get(tier):
            break
        else:
            print("Invalid membership type.")
    print(f"Your fee is £{level}/month")
    
def record_payment():
    while True:
        try:
            m_id = int(input("Enter your ID: "))
            member = members.get(m_id)
            if member:
                while True:
                    try:
                        amount = float(input("Enter the payment amount: "))
                        break    
                    except:
                        print("Enter a valid monetary amount.")
                    id = len(payments)
                    payments.update({id:{"member":m_id,"amount":amount,"time":datetime.now()}})
                break
                
            else:
                print("Not a valid member")
        except ValueError:
            print("Enter a valid ID")
    
    now = datetime.now()
    print("Done! Payment submitted at", now.strftime("%I:%M %p"))
        
menu = """
--- Gym App -------------
    (1) Register member
    (2) View types
    (3) Calculate fee
    (4) Record payment
    (5) Exit
------------------------------
"""

menu_dict = {
    1: register,
    2: view_types,
    3: calculate_fee,
    4: record_payment,
    5: exit
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