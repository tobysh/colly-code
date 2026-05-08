import pandas as pd
import matplotlib.pyplot as plt
from modules.get_file_path import get_path

#load csv
df = pd.read_csv(get_path(file_name="employees.csv"))


menu= """
1. Employees in a department
2. Salary per department
3. Compare Salaries
"""

def employeesInDept():
      departments = df["Department"].unique()
      department = ""
      while department not in departments:
            department = input("Enter the department:\n>")
      employees = df[df["Department"]==department]["Name"]
      print(employees)

def salaryPerDepartment():
      departments = df["Department"].unique()
      department = ""
      while department not in departments:
            department = input("Enter the department:\n>")
      employees = df[df["Department"]==department]["Name"]
      salaries = df[df["Department"]==department]["Salary"]
      plt.bar(employees, salaries)
      plt.title("Salary of employees")
      plt.xlabel("Employee")
      plt.ylabel("Salary")
      plt.show()

def compareSalaries():
      departments = df["Department"].unique()
      department = ""
      department2 = ""
      while department not in departments:
            department = input("Enter the department:\n>")
      while department2 not in departments:
            department2 = input("Enter the department:\n>")
      meanPerDepartment = df.groupby("Department")["Salary"].mean()
      first = meanPerDepartment[department]
      second = meanPerDepartment[department2]
      plt.bar([department, department2], [first, second])
      plt.title("Salary by Department")
      plt.xlabel("Department")
      plt.ylabel("Salary")
      plt.show()

choices = {
      "1":employeesInDept,
      "2":salaryPerDepartment,
      "3":compareSalaries
}
print(menu)
choice = ""
while choice not in choices.keys():
      choice = input("Enter a choice from the list:\n>")
choices[choice]()