import sqlite3

con = sqlite3.connect("students.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Courses(" \
"CourseID INTEGER PRIMARY KEY AUTOINCREMENT," \
"CourseName TEXT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS Students(" \
"StudentID INTEGER PRIMARY KEY AUTOINCREMENT," \
"Name TEXT NOT NULL," \
"Age int," \
"CourseID int," \
"CONSTRAINT fk_course FOREIGN KEY (courseID) REFERENCES Courses(CourseID))")
