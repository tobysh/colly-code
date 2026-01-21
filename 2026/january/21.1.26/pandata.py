from modules.get_file_path import get_path
import pandas as pd

path = get_path(file_name="pandas_data_1.csv")

df = pd.read_csv(path)
print(df["Duration"].mode())
dur = int(input("What duration would you like to query?\n>"))
dft = df[df["Duration"]==dur]["Duration"]

print(f"There were {dft.count()} workouts lasting {dur} minutes")