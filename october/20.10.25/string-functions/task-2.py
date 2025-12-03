import json
configFile = True
replaceWord = "bad"
replaceWith = "good"
findWord = "chicken"
if configFile:
    with open("/workspaces/colly-code/20.10.25/task-2-config.json","r") as file:
        config = file.read()

    config = json.loads(config)
    replaceWord = config["replace"][0]
    replaceWith = config["replace"][1]
    findWord = config["findWord"]
    print(replaceWord, replaceWith, findWord)
paragraph = input("Write a short sentence or paragraph: ")
print(f"Found {findWord} at position {paragraph.find(findWord)}")
print(paragraph.replace(replaceWord, replaceWith))