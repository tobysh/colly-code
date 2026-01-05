class Student:
    def __init__(self, studentName, age, studentId, subject):
        self.StudentName = studentName,
        self.age = age
        self.studentId = studentId
        self.subject = subject
    def __str__(self):
        return(f"Name: {self.StudentName}, id: {self.studentId}, age: {self.age}, subject: {self.subject}")
    
students = []
students.append(Student(studentName="ethan",age=17,studentId="1782818",subject="Software engineering"))
print(students[0])