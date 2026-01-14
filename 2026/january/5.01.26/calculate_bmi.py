def calculate_bmi(weight, height): 
    bmi = weight / height**2 
    if bmi < "25": 
        status = Healthy 
    else: 
        status = "Overweight" 
    return status 

w = 80 
h = 1.75 
print(calculate_bmi(w, h)) 