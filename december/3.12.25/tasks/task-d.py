import os
import sys

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
file_path = os.path.join(script_directory,"assets","scores.txt")


data = []
scores = []
for i in range(5):
    name = input("Enter a name: ")
    score = score2 = -1
    while score == -1 or score2 == -1:
        try:
            score = int(input("Enter your score: "))
            score2 = int(input("Enter your second score: "))
            scores = [score, score2]
        except:
            print("Enter a valid number")
    data.append([name, scores])

with open(file_path, "w") as file:
    for item in data:
        file.write(f"{item[0]},{item[1]}\n")

scores_dict = {}

with open(file_path, "r") as file:
    data = file.readlines()
    scores = []
    for item in data:
        score = item.strip().split(",")[1:]
        score = [int(score[0][1]), int(score[1][1])]
        scores.append(score)
        name = item.strip().split(",")[0]
        scores_dict.update({name:score})
print(scores_dict)

for item in scores_dict.items():
    score = item[1]
    avg = sum(score)/2
    print(f"{item[0]} average: {avg}")
