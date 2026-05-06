from modules.get_file_path import get_path
import pandas as pd
import matplotlib.pyplot as plt

#load csv
df = pd.read_csv(get_path(file_name="employees.csv"))

#Task A
sel = df.iloc[0:5,0:3]
print(sel)
print()

#Task A2
sel = df.iloc[9:20,1:5]
print(sel)
print()

#Task A3
sel = df.iloc[[0,5,10,15],[2,4]]
print(sel)
print()

#Task A4
sel = df.iloc[:, 4]
print(sel)
print()

#Task A5
sel = df.iloc[-10:, -2:]
print(sel)
print()

#Task B
df.set_index('EmployeeID', inplace=True)
sel = df.loc["E010":"E020"]
print(sel)
print()

#Task B2
sel = df.loc[["E005","E015","E025"],["Name", "Salary", "Department"]]
print(sel)
print()

sel = df[df["Salary"]>40000]
print(sel)
print()

sel = df[(df["Department"]=="IT")| (df["Department"]=="Finance")]
print(sel)
print()

