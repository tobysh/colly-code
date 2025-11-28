items=[2,3,8,9,12,22,33,45,200]

target = int(input("Number to search for: "))
low = 0
high = len(items)-1
mid = (low+high)//2
found = False
while high >= low:
    if items[mid] < target:
        low = mid+1
        mid = (low+high)//2
    elif items[mid] > target:
        high = mid-1
        mid = (low+high)//2
    else:
        print(f"Found {target} as position {mid}")
        found = True
        break

if not found:
    print(f"{target} was not found")