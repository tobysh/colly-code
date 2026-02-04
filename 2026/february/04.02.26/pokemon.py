#TASK 1
import pandas as pd
from modules.get_file_path import get_path

df = pd.read_csv(get_path(file_name="pokemon.csv"))

print(f"---Task 1.3---\n{df.head}")

#TASK 2
print(f"---Task 2.1---\n{df.shape}")
print(f"---Task 2.2---\n{df.columns}")
print(f"---Task 2.3---\nInfo: {df.info()}\nDescribe: {df.describe()}")

#TASK 3
fireTypes = df["Type_1"].value_counts().get("Fire", 0)
print(f"---Task 3.1---\n{fireTypes}")
waterFlying = df[(df["Type_1"]=="Water") & (df["Type_2"]=="Flying")]["Name"]
print(f"---Task 3.2---\n{waterFlying}")
print("---Task 3.3---")

type = input("Enter the type you are searching for: ").strip().capitalize()
userType = df[(df["Type_1"]==type)]
print(userType.all)

speedyPokemon = df[(df["Speed"]>100)]
print(speedyPokemon)

#TASK 4
print(f"---Task 4---\n{df.iloc[0:10,0:5]}")