students=[
    {
        "name":"Ethan",
        "scores":[50,60,40]
    },
    {
        "name":"Shea",
        "scores":[20,40,30]
    },
    {
        "name":"Boggy",
        "scores":[60,70,80]
    }
]


for student in students:
    print(f"{student.get('name')}: {sum(student.get('scores'))/len(student.get('scores'))}")

