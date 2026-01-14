def check_output(actual, target): 
    if actual < target:
        print("Under target") 
    elif actual >= target:
        print("On target") 
    else:
        print("Under target") 

actual_output = 950 
target_output = 1000 

check_output(actual_output, target_output) 