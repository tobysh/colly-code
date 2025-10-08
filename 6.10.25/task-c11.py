students = {
    "John":67,
    "Ron":41,
    "Don":69
}

def lookup():
    name = input("Enter a student's name to look up their grade: ").capitalize()
    grade = students.get(name)
    if grade == None:
        print(f"Student '{name}' was not found")
    else:
        print(f"Student '{name}' has the grade {grade}")

def add_student():
    name = input("Enter the name of the student you would like to add: ").capitalize()
    try:
        grade = int(input("Enter the students grade: "))
        students.update({name: grade})
    except TypeError:
        print("Grade is a number, please do not use alphabetical characters.")

def view_students():
    for i in students:
        print(f"{i}: {students[i]}")

optionsMap = {
    '1':lookup,
    '2':add_student,
    '3':view_students
}

while True:
    print("----------")
    options = """
(1) Look up student,
(2) Add student,
(3) View all students
"""
    print(options)
    choice = input(">")
    try:
        optionsMap[choice]()
    except KeyError:
        print("Entry was not a valid option")
