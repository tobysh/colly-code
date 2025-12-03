"""
Create your own program with validation:
• Input a student's exam grade.
• Apply the following checks:
• Type check (must be integer).
• Range check (0-100).
• Presence check (cannot be blank).
• Print if the grade is valid
"""
valid = False
while not valid:
    grade = input("Enter your mark: ").strip()
    if grade != "":
        if grade.isdigit():
            if int(grade) >= 0 and int(grade) <= 100:
                valid = True
            else:
                print("mark out of range.")
        else:
            print("mark is not a valid integer.")
    else:
        print("mark is empty.")

print("Valid mark")
