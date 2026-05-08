from modules.get_file_path import get_path
import pandas as pd
import matplotlib.pyplot as plt

#load csv
df = pd.read_csv(get_path(file_name="employees.csv"))

#Task A
sel = df.iloc[0:4,0:2]
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

#Task B3
sel = df[df["Salary"]>40000]
print(sel)
print()

#Task B5
sel = df[(df["Department"]=="IT")| (df["Department"]=="Finance")]
print(sel)
print()

#Task B6
sel = df[(df["PerformanceScore"] >= 4)& (df["YearsExperience"]>5)]
print(sel)
print()

#Task C
sel = df[df["Age"]<30]
print(sel)
print()

#Task C2
sel = df[(df["Salary"]>35000) & (df["Salary"]<45000)]
print(sel)
print()

#Task C3
sel = df[(df["Department"]=="Sales") & (df["PerformanceScore"]==5)]
print(sel)
print()

#Task C4
HighPerformers = df[df["PerformanceScore"]>= 4]
print(HighPerformers)
print()

#Task D1
plt.plot(range(len(df["Salary"])),df["Salary"])
plt.xlabel("EmployeeID")
plt.ylabel("Salary")
plt.show()

#Task D2
avgSalary = df.groupby("Department")["Salary"].mean()
#print(avgSalary)
plt.bar(avgSalary.index, avgSalary.values)
plt.title('Salary by Department') 
plt.xlabel('Department') 
plt.ylabel('Salary') 
plt.show()

#Task D3
employeesByDepartment = df.groupby("Department").count()["Name"]
plt.pie(employeesByDepartment,labels=employeesByDepartment.index)
plt.show()

#Task E
salaryUnder30=df[df["Age"]<30]["Salary"]
#print(avgSalary)
plt.bar(salaryUnder30.index, salaryUnder30.values)
plt.title('Salary by Department') 
plt.xlabel('Department') 
plt.ylabel('Salary') 
plt.show()

#Task E2

plt.plot(range(len(df[df["Department"]=="IT"])),df[df["Department"]=="IT"]["Salary"])
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.title("IT Department Salaries")
plt.show()

#Task E3
plt.pie(HighPerformers.value_counts(), labels=HighPerformers.index)
plt.show()

#Task F
finance = df.set_index("Department")
finance = finance.loc["Finance"]
finance.set_index('Name', inplace=True)
print(finance)
plt.bar(finance.index, finance["Salary"])
plt.xlabel('Name') 
plt.ylabel('Salary') 
plt.title("Finance Salaries")
plt.show()

#Task F2
plt.title("Subset Salaries")
subset = df.iloc[[0,5,10,15,20],:]
plt.plot(subset["Name"],subset["Salary"])
plt.xlabel('Name') 
plt.ylabel('Salary') 
plt.show()

#Task F3
plt.title("Filtered Salaries")
filtered = df[df["Salary"]>40000]
plt.bar(filtered["Name"],filtered["Salary"])
plt.xlabel('Name') 
plt.ylabel('Salary') 
plt.show()

#Task G
meanPerDepartment = df.groupby("Department")["Salary"].mean()
highestSalary = df["Salary"].max()
lowestSalary = df["Salary"].min()
print(f"""
Mean per department:\n{meanPerDepartment}\n\n
Highest Salary: {highestSalary}
Lowest Salary: {lowestSalary}
      """)

#Task G2
salaryByExperience=df.groupby("YearsExperience")["Salary"].mean()
print(round(salaryByExperience,3))
plt.bar(salaryByExperience.index, salaryByExperience.values)
plt.title("Salary By Experience")
plt.xlabel("Years Experience")
plt.ylabel("Average Salary")
plt.show()
