from modules.get_file_path import get_path
import pandas as pd

df = pd.read_csv(get_path("assets","pandas_data_1.csv")) #1a

print(df.head) #1b
print(df.tail) #1c

print(df.shape) #1d
print(df.describe()) #1e

df_calories = df['Calories'] #1f
df_duration_calories = df[['Duration', 'Calories']] #1g
df_mid = df.iloc[[4,17]] #1i
df_1j = df.iloc[9][["Duration", "Pulse"]] #1j
df_1k = df.iloc[[10,20]] #1k
df_1L = df.iloc[[9,19]][["Pulse","Calories"]] #1l
print(f"💠---Task 1f---\n{df_calories}")
print(f"💠---Task 1g---\n{df_duration_calories}")
print(f"💠---Task 1h---\n{df.dtypes}") #1h
print(f"💠---Task 1i---\n{df_mid}")
print(f"💠---Task 1j---\n{df_1j}")
print(f"💠---Task 1k---\n{df_1k}")
print(f"💠---Task 1l---\n{df_1L}")


#Task 2, The difference between df.iloc[10:20] and df.loc[10:20] is that iloc begins indexing at 0 while loc begins indexing at 1, meaning iloc has 1 earlier index.