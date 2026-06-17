import sqlite3
import os

filename = "warehouse.db"
if os.path.exists(filename):
    os.remove(filename)

con = sqlite3.connect(filename)
cur = con.cursor()
def create():
    cur.execute("""CREATE TABLE Customers(
                CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
                FirstName VARCHAR(255) NOT NULL,
                LastName VARCHAR(255) NOT NULL,
                Email VARCHAR(255) NOT NULL,
                Phone VARCHAR(255) NOT NULL,
                DeliveryAddresses VARCHAR(255) NOT NULL,
                City VARCHAR(255) NOT NULL,
                Postcode VARCHAR(255) NOT NULL,
            )
                """)
    
    cur.execute("""
CREATE TABLE Suppliers(
                SupplierID INTEGER PRIMARY KEY AUTOINCREMENT,
                SupplierName VARCHAR(255),
                ContactName VARCHAR(255),
                Email VARCHAR(255),
                Phone VARCHAR(255),
                Address VARCHAR(255))
""")
    
    cur.execute("""
CREATE TABLE Warehouses(
                WarehouseID INTEGER PRIMARY KEY AUTOINCREMENT,
                WarehouseName VARCHAR(255),
                Location VARCHAR(255),
                MaxCapacity INTEGER)
""")
    
    cur.execute("""
CREATE TABLE Products(
                ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
                ProductName VARCHAR(255),
                Description TEXT,
                UnitPrice DECIMAL(10,2)
                )
""")
    
    cur.execute("""
CREATE TABLE Orders(
                OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
                CustomerID INTEGER,
                OrderDate VARCHAR(255),
                Status VARCHAR(255),
                CONSTRAINT fk_customerid FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
""")
    
    cur.execute("""
CREATE TABLE OrderLine(
                OrderLineID INTEGER PRIMARY KEY AUTOINCREMENT,
                OrderID INTEGER,
                ProductID INTEGER,
                WarehouseID INTEGER,
                StockLevel INTEGER)
                """)
    
    cur.execute("""
CREATE TABLE Inventory(
                InventoryID INTEGER PRIMARY KEY AUTOINCREMENT,
                ProductID INTEGER,
                WarehouseID INTEGER,
                StockLevel INTEGER,
                
                CONSTRAINT fk_product FOREIGN KEY (ProductID) REFERENCES Warehouses(WarehouseID),
                CONSTRAINT fk_warehouse FOREIGN KEY (WarehouseID) REFERENCES Products(StockLevel))

""")

    cur.execute("""
CREATE TABLE Shipments(

                ShipmentID INTEGER PRIMARY KEY AUTOINCREMENT,
                SupplierID INTEGER
                WarehouseID INTEGER,
                DeliveryDate VARCHAR(255),
                CONSTRAINT fk_supplier FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
                CONSTRAINT fk_warehouse FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID),
                )
""")