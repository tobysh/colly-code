animals = {
    "dog":"woof",
    "cat":"meow",
    "cow":"moo"
}

choice = animals.get(input("Enter an animal\n"))
if choice != None:
    print(choice)
else:
    print("I don\'t know that animal sound")