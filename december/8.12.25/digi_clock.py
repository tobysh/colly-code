palindromic_times = []
for h in range(24):
    for m in range(60):
        time = f"{h:02}:{m:02}"
        if time[::-1] == time:
            palindromic_times.append(time)
inp_time = None
while inp_time == None:
    inp_time = input("Enter the time in HH:MM format: ").split(":")
    if len(inp_time)[0] != 2 or len(inp_time)[1] != 2:
        inp_time = None