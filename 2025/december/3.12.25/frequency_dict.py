numbers = []
while True:
    try:
        num = int(input("Enter a number (-1 to escape the loop): "))
    except ValueError:
        continue
    if num == -1:
        break
    else:
        numbers.append(num)
    
frequency = {}
for number in numbers:
    count = 0
    for num in numbers:
        if number == num:
            count += 1
    frequency.update({f"{number}":count})
for x, y in frequency.items():
  print(f"{x}: {y}")