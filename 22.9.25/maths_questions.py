import random
questions = []

bound_mapping = {
    "x": 12,
    "/": 12,
    "-": 100,
    "+": 100
}

def validate_numbers(first_number, second_number, operator):
    first_num = first_number
    second_num = second_number
    if operator == "-":
        while first_num - second_num < 0:
            first_num = random.randint(1,bound_mapping[operator])
            second_num = random.randint(1,bound_mapping[operator]) 
    if operator == "/":
        while first_num % second_num != 0 or first_num == second_num or first_num == 1 or second_num == 1:
            first_num = random.randint(1,bound_mapping[operator])
            second_num = random.randint(1,bound_mapping[operator])
    if operator == "x":
        while first_num == 1 or second_num == 1:
            first_num = random.randint(2,bound_mapping[operator])
            second_num = random.randint(2,bound_mapping[operator])
    return (first_num, second_num)

def generate_question():
    operations = ["+", "-", "x", "/"]
    operator = random.choice(operations)
    first_number = random.randint(1,bound_mapping[operator])
    second_number = random.randint(1,bound_mapping[operator])
    (first_number, second_number) = validate_numbers(first_number, second_number, operator)
    question = f"{first_number}{operator}{second_number}"
    question_mapping = {
        "+": first_number+second_number,
        "-": first_number-second_number,
        "x": first_number*second_number,
        "/": first_number//second_number
    }
    answer = question_mapping[operator]
    return [question, answer]

for i in range(5):
    questions.append(generate_question())

score = 0
for i in range(len(questions)):
    answer = (int(input(f"{questions[i][0]}: ")))
    if answer == questions[i][1]:
        score += 1
        print("Correct!")
    else:
        print("Wrong, answer is",questions[i][1])

print(f"Your score is {score}")