st1Name = input("Enter Name: ")
t1Mark = input(f"Enter mark for {st1Name}: ")
with open("etc/marks.txt", "w") as f:
    f.write("Alice,85\n")
    f.write("Bob,74\n")
    f.write(f"{st1Name},{t1Mark}\n")
    
with open("etc/marks.txt", "r") as f:
    for line in f:
        name, mark = line.strip().split(",") # saving in 2 lists
        print(name, "scored ",mark)
