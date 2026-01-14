response={
    "happy":"That\'s great! Keep smiling!",
    "tired":"Take a break and rest.",
    "sad":"That\'s not great, try to talk to someone"
}

output = response.get(input("How are you feeling today?\n>").lower().strip())
if output == None:
    print("Invalid mood")
else:
    print(output)