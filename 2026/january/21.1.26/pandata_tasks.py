from modules.get_file_path import get_path
import pandas as pd

path = get_path(file_name="pandas_data_1.csv")

df = pd.read_csv(path)
#print(df["Duration"].mode())
#dur = int(input("What duration would you like to query?\n>"))
#dft = df[df["Duration"]==dur]["Duration"]

#print(f"There were {dft.count()} workouts lasting {dur} minutes")

#a
dft = df[df["Duration"]==60]["Duration"]
print(f"There were {dft.count()} workouts lasting 60 minutes")
dft = df[df["Duration"]==45]["Duration"]
print(f"There were {dft.count()} workouts lasting 45 minutes")
#b
print(f"{df["Duration"].mode()}")
#c
dft = df[df["Pulse"]==100]["Pulse"]
print(f"There were {dft.count()} workouts with a pulse of exactly 100")
#d
dft = df["Calories"]
print(f"There were {dft.isnull().sum()} workouts with missing calorie values")
#e
dft = df[df["Duration"]<=30]["Duration"]
print(f"There were {dft.count()} workouts lasting 30 minutes or less")
#f
dft = df[df["Pulse"]>150]["Pulse"]
print(f"There were {dft.count()} workouts with a pulse greater than 150")
#g
dft = df[df["Calories"]>400]["Calories"]
print(f"There were {dft.count()} workouts that burnt more than 400 calories")
#h
dft = df.groupby("Duration")["Duration"]
print(f"{dft.count()}")
#i
dft = df[df["Duration"]==60]["Duration"].count()
dft2 = df[df["Duration"]!=60]["Duration"].count()
if dft > dft2:
    print("There are more 60 minute workouts")
elif dft < dft2:
    print("There are more workouts of different durations")
else:
    print("They are the same")