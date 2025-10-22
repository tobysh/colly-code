start = int(input("Start number: "))
end = int(input("End number: "))+1
for n in range(start, end):
    print(f"Times table for {n}")
    for i in range(1, 13):
        print(n, "x", i, "=", n * i)
