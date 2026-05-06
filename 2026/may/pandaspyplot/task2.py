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