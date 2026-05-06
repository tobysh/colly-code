import pandas as pd
import matplotlib.pyplot as plt
from modules.get_file_path import get_path

#loading csv file into the dataframe
path = get_path(file_name="handout.csv")
df = pd.read_csv(path)
print()

#Task 1
selection = df.iloc[[-2,-1], [0,1]]
print(selection)
print()

#Task 2
selection = df.iloc[[0,2],[1,3]]
print(selection)
print()

#Task 3
selection = df.iloc[:,2]
print(selection)
print()

#loc
#Task 1
selection = df.loc["Bob":"Ethan", ["Name", "Department"]]
print(selection)
print()

#Task 2
df2 = df
df2.index = ["Alice","Bob", "Charlie","Diana","Ethan"]
selection = df2.loc[["Alice","Diana"], :]
print(selection)
print()

#Task 3
selection = df.loc[df["Salary"]>30000, :]
print(selection)
print()

#plt
#Task 1

names= df["Name"]
age = df["Age"]
plt.bar(names, age)
plt.show()

#Task 2
evenProportion = []
for i in range(len(df["Department"])):
    evenProportion.append((100/len(df["Department"])))
    
plt.pie(evenProportion, labels=df['Department'], autopct='%1.1f%%') 
plt.show()

#Task 3
selection = df[df["Age"]<30]

plt.plot(selection["Name"], selection["Salary"])
plt.title("Salary by worker under 30")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.show()
