import sqlite3
import os

if os.path.exists("members.db"):
    os.remove("members.db")

con = sqlite3.connect("members.db")
cur = con.cursor()
def create():
    cur.execute("CREATE TABLE IF NOT EXISTS Books(" \
    "BookID INTEGER PRIMARY KEY AUTOINCREMENT," \
    "Title TEXT(100) NOT NULL," \
    "Author TEXT(50) NOT NULL," \
    "Genre TEXT(30) NOT NULL," \
    "ISBN TEXT(20) NOT NULL)")

    cur.execute("CREATE TABLE IF NOT EXISTS Members(" \
    "MemberID INTEGER PRIMARY KEY AUTOINCREMENT," \
    "FirstName TEXT NOT NULL," \
    "LastName TEXT NOT NULL," \
    "Email TEXT NOT NULL," \
    "Phone TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS Loans(" \
    "LoanID INTEGER PRIMARY KEY AUTOINCREMENT," \
    "BookID INTEGER," \
    "MemberID INTEGER," \
    "LoanDate TEXT," \
    "ReturnDate TEXT," \
    "CONSTRAINT fk_book FOREIGN KEY (BookID) REFERENCES Books(BookID)," \
    "CONSTRAINT fk_member FOREIGN KEY (MemberID) REFERENCES Members(MemberID))")

create()

cur.execute("ALTER TABLE Members RENAME COLUMN MemberID TO BorrowerID;")
cur.execute("ALTER TABLE Members RENAME TO Borrowers;")
cur.execute("ALTER TABLE Borrowers ADD COLUMN JoinDate TEXT;")
cur.execute("ALTER TABLE Borrowers ADD COLUMN ParentConsent Boolean;")
cur.execute("ALTER TABLE Books RENAME COLUMN Title TO BookTitle;")
cur.execute("ALTER TABLE Books DROP COLUMN ISBN;")
cur.execute("ALTER TABLE Loans ADD COLUMN Returned TEXT;")

cur.execute("DROP TABLE Borrowers;")
cur.execute("DROP TABLE Books;")
cur.execute("DROP TABLE Loans;")

create()

cur.execute("ALTER TABLE Members RENAME TO LibraryUsers")
cur.execute("ALTER TABLE LibraryUsers RENAME COLUMN MemberID TO UserID")
cur.execute("ALTER TABLE LibraryUsers ADD COLUMN JoinDate")
cur.execute("ALTER TABLE Books RENAME COLUMN Title TO BookTitle;")
cur.execute("ALTER TABLE Books DROP COLUMN ISBN;")
cur.execute("ALTER TABLE Books ADD COLUMN ShelfLocation TEXT")
cur.execute("ALTER TABLE Loans ADD COLUMN Returned BOOLEAN;")
cur.execute("ALTER TABLE Loans RENAME COLUMN MemberID TO UserID")

