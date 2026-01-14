import math
gravity = 9.8
height = float(input("Enter the height the items being dropped from (m): "))

velocity = math.sqrt(2*gravity*height)

print(f"The velocity is {velocity}m/s")