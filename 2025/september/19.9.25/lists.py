overal= int(input("Enter total possible mark"))
marks = []
for i in range(10):
    m = int(input(f"Enter mark for student {i+1}: "))
    marks.append(m)
for i in range(len(marks)):
    print(f"Student {i+1} got {(marks[i]/overal)*100}%")