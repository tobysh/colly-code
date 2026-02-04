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

#TASK 5
df["Power_index"] = df["Attack"]+df["Defense"]+df["Speed"]
print(f"---Task 5.1---")
print(df.head())
df["is_strong"]=df["Power_index"]>250
print(f"---Task 5.2---")
print(df.head())

#TASK 6
print(f"---Task 6.1---")
sorted_speed = df.sort_values("Speed", ascending=False)
print(sorted_speed.head())
print(f"---Task 6.2---")
sorted_hp = df.sort_values("HP")
print(sorted_hp.head())
sorted_defense = df.sort_values("Defense")
print(sorted_defense.head())
sorted_total = df.sort_values("Total", ascending=False)
print(f"---Task 6.3---\n{sorted_total.head(10)}")