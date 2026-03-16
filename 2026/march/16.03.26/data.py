import pandas as pd
from matplotlib import pyplot

df= pd.read_csv(r"11 Data Analysis Flowchart Design and Implementation.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
df["High_Sales"] = df["Sales"] > 200
df["Revenue_Per_Item"]=df["Sales"]/df["Quantity_Sold"]

def calculate_average_all(df):
    return round(df["Price"].mean(), 2)

def avg_for_product(df):
    name = input("Enter the product name: ")
    return round(df[df["Product"]==name]["Quantity_Sold"].mean(),2)

def avg_qs_sales(df):
    avg_qs = df["Quantity_Sold"].mean()
    avg_sales = df["Sales"].mean()
    return f"Average quantity: {avg_qs},\nAverage sales: {avg_sales}"

def find_max_min(df):
    col = input("Enter a column out of Price, Quantity_Sold or Sales")
    if col not in ["Price", "Quantity_Sold", "Sales"]:
        print("Invalid Column name")
        return("Error")
    min = df[col].min()
    max = df[col].max()
    return(f"The minimum value for {col} is {min} and the maximum value is {max}")

def count_sales_by_product(df):
    quant=(df.groupby("Product")["Quantity_Sold"].sum())
    rev = df.groupby("Product")["Sales"].sum()


func_map = {
    "1": calculate_average_all,
    "2": avg_for_product,
    "3": avg_qs_sales,
    "4": find_max_min
}
def menu():
    prompt = """
    1. Calculate the Average (mean) Price,
    2. Calculate the Average Quantity Sold for a Product,
    3. Calculate the Average Quantity Sold and Sales,
    4. Find the Minimum and Maximum Values,
    5. Count Total Sales by Product,
    6. Display High Sales Transactions,
    7. Generate Data Visualisations
    8. Exit Program
    """
    
    print(prompt)
    
    option = input(">")
    print(func_map[option](df))
    menu()
    
count_sales_by_product(df)