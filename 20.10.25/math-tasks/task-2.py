import math

side_a = float(input("Enter one side of your right-angled triangle (cm): "))
side_b = float(input("Enter another side of your right-angled triangle (cm): "))

side_c = math.sqrt(math.pow(side_a,2)+math.pow(side_b,2))

print(str(side_c)+"cm")