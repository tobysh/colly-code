patients = {
    
}

def register_patient():
    name = input("Enter the patient name: ").capitalize()
    if input("Enter \"Y\" to confirm entry\n>").upper() == "Y":
        patients.update({name:"Unassigned"})
    else:
        print("Operation cancelled.")

def view_patient_count():
    print(f"There are {len(patients.keys())} patients currently.")

def assign_ward():
    name = input("Enter the patient name\n>").capitalize()
    if not patients.get(name):
        print("Patient not found.")
    else: 
        wards = ["north", "south", "east", "west"]
        print("Possible wards: North, South, East, West")
        ward = input("Enter a ward to place the patient in.\n>").lower()
        if ward in wards:
            if input("Enter \"Y\" to confirm entry\n>").upper() == "Y":
                patients.update({name: ward})
                print(f"Successfully placed {name} in the {ward} ward.")
            else:
                print("Operation cancelled.")
        else:
            print("Invalid ward.")
        
menu = """
--- Hospital app -------------
    (1) Register patient
    (2) View patient Count
    (3) Assign ward
    (4) Exit
------------------------------
"""

menu_dict = {
    1: register_patient,
    2: view_patient_count,
    3: assign_ward,
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