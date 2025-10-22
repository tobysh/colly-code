import json
configFile = True
if configFile:
    with open("/workspaces/colly-code/20.10.25/task-5-config.json","r") as file:
        config = file.read()

    config = json.loads(config)
    trailingPhrase = config["trailingPhrase"]
    countWord = config["countWord"]
    print(trailingPhrase, countWord)
else:
    trailingPhrase = "beans"
    countWord = "apples"
blockOfText=input("Enter a block of text: ")
print(f"The word {countWord} appears {blockOfText.count(countWord)}")
if blockOfText.endswith(trailingPhrase):
    print("The text does end with", trailingPhrase)
else:
    print("The text does not end with", trailingPhrase)