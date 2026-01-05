def sum_odd(numbers:list):
    out = 0
    for num in numbers:
        if num%2==1:
            out += num
            
    return out

numbers=[1,3,5,2,4,2,1,7]
print(sum_odd(numbers))
