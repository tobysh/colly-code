import pandas as pd
import matplotlib.pyplot as plt
from modules.get_file_path import get_path


def menu():
  while(True):
    print("1: Task 1\n")
    print("2: Task 2\n")
    print("3: Task 3\n")
    print("4: Task 4\n")
    print("5: Task 5\n")
    print("6: Task 6\n")
    print("7: Task 7\n")
    print("8: Task 8\n")
    print("9: Task 9\n")
    print("10: Task 10\n")
    print("11: Task 11\n")
    print("0: Exit\n")
    choice= int(input("Your Choice:    "))
    df=load_prep_data()
    if choice==1:
      task1(df)
    elif choice==2:
      task2(df)
 
def load_prep_data():
  # Load data
  df = pd.read_csv(get_path(file_name="12.PSLseason2425.csv"))
  df["Date"] = pd.to_datetime(df["Date"], format='%d/%m/%Y')
  df["GoalDifference"] = df["FullTimeHomeTeamGoals"] + df["FullTimeAwayTeamGoals"]
  df["GoalDifference"] = df["FullTimeHomeTeamGoals"] - df["FullTimeAwayTeamGoals"]
  return df
 
def task1(df):
  refName = input("What\'s the name of the referee?").strip()
  cards = df.loc[df["Referee"] == refName, ["HomeTeamYellowCards", "AwayTeamYellowCards", "HomeTeamRedCards", "AwayTeamRedCards"]].sum()
  reds = cards["HomeTeamRedCards"] + cards["AwayTeamRedCards"]
  yellows = cards["HomeTeamYellowCards"] + cards["AwayTeamYellowCards"]
  print(f"{refName} has given out {yellows} yellow cards and {reds} red cards")
 
def task2(df):
  teamName = input("What\'s the team name?").strip()
  home = (df.loc[df["HomeTeam"] == teamName, ["FullTimeResult"]]=="H").count()
  print(home)
 
def task3(df):
  print("WIP")
 
def task4(df):
  print("WIP")
 
menu()