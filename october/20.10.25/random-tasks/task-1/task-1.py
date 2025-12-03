import random
import json

def load_words(path):
    with open(path, "r") as file:
        words = file.readlines()
    for i in range(len(words)):
        words[i]=words[i].rstrip()
    return words

adjectives = load_words("/workspaces/colly-code/20.10.25/random-tasks/task-1/wordLists/english-adjectives.txt")
nouns = load_words("/workspaces/colly-code/20.10.25/random-tasks/task-1/wordLists/english-nouns.txt")
places = load_words("/workspaces/colly-code/20.10.25/random-tasks/task-1/wordLists/english-cities.txt")
with open("/workspaces/colly-code/20.10.25/random-tasks/task-1/wordLists/infinitiv-verbs-list.json") as file:
    verbs = json.loads(file.read())

adjective = random.choice(adjectives)
noun = random.choice(nouns)
verb = random.choice(verbs)
place = random.choice(places)

print(f"""Once upon a time, a {adjective} {noun} chose to {verb} in {place}. The 
{noun} went to {place} and started to {verb} like a {adjective} hero. 
Everyone in {place} was shocked when the {adjective} {noun} began to 
{verb}. Nobody expected the {noun()} to {verb} so {adjective}ly in {place}.""")