students = {
    
}

def add_student():
    name = input("Enter the student name: ").capitalize()
    try:
        temp_group = int(input("Enter the year group: "))
    except ValueError:
        print("Not a valid number.")
    if temp_group > 13 or temp_group < 1:
        print("Not a valid year group.")
    else:
        if input("Enter \"Y\" to confirm entry\n>").upper() == "Y":
            students.update({name:{"attendance":100,"year":temp_group}})
        else:
            print("Operation cancelled.")

def view_attendance():
    name = input("Enter the student name\n>").capitalize()
    if not students.get(name):
        print("student not found.")
    attendance = students.get(name)["attendance"]
    print(attendance)
    
def calculate_average():
    nums = []
    for i in range(3):
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("Not a valid number.")
        nums.append(num)
    print(sum(nums)/len(nums))
        
menu = """
--- School Admin App -------------
    (1) Add student
    (2) View attendance
    (3) Calculate average
    (4) Exit
------------------------------
"""

menu_dict = {
    1: add_student,
    2: view_attendance,
    3: calculate_average,
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