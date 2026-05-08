import tkinter as tk
from tkinter import simpledialog, messagebox

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
            # Entry widget
            department = simpledialog.askstring("Input", "Enter the department:").strip()

            if not department or department not in departments:
                  messagebox.showwarning("Warning", "Input is invalid!")
                  return
            employees = df[df["Department"]==department]["Name"]
            messagebox.showinfo(employees)

      

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

root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x150")  # Width x Height

# Create and place a label
label = tk.Label(root, text="Choose an option", font=("Arial", 12))
label.pack(pady=5)

# Create and place a button
button = tk.Button(root, text="Employees in a department", command=employeesInDept)
button.pack(pady=10, expand=True)

# Start the Tkinter event loop
root.mainloop()