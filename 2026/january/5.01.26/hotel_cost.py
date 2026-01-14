def room_cost(nights, rate): 
    if nights >=5:
        discount = 0.1 
    else: 
        discount = 0 
    total_cost = nights * rate * (1 - discount) 
    return total_cost 

nights = 4
rate = 120 
print(room_cost(nights, rate)) 