score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))

final_grade = (score1 * 0.5) + (score2 * 0.25) + (score3 * 0.25)

if 75 <= final_grade <= 100:
    grade = "A"
elif 60 <= final_grade < 75:
    grade = "B"
elif 50 <= final_grade < 60:
    grade = "C"
elif 40 <= final_grade < 50:
    grade = "D"
elif 0 <= final_grade < 40:
    grade = "F"
else:
    grade = "Invalid score"

print(f"Final Grade: {grade}")