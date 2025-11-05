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
grade = input("Enter your grade: ").strip()
if grade != "":
    if grade.isdigit():
        if int(grade) >= 0 and int(grade) <= 100:
            valid = True

if valid:
    print("Valid grade")
else:
    print("Invalid grade")