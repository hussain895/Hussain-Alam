
class Student:
    def __init__(self, student_id, name, course, grade):    
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grade = grade    
    def student_id(self):
        return self.student_id
    def grade(self):
        return self.grade
    def display_info(self):
        print(f"Student ID: {self.student_id}, Name: {self.name}, Course: {self.course}, Grade: {self.grade}")
       

students = []
num_students = int(input("Enter the number of students: "))
for _ in range(num_students):
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    grade = float(input("Enter Grade (0-100): "))
    student = Student(student_id, name, course, grade)
    students.append(student)

for student in students:
    if 90 <= student.grade <= 100:
        print(f"{student.name} has received an A.")
    elif 80 <= student.grade < 90:
        print(f"{student.name} has received a B.")
    elif 70 <= student.grade < 80:
        print(f"{student.name} has received a C.")
    elif 60 <= student.grade < 70:
        print(f"{student.name} has received a D.")
    elif 0 <= student.grade < 60:
        print(f"{student.name} has received an F.")
    else:
        print(f"Invalid grade for {student.name}.")

import csv
filename = "students.csv"
with open(filename, "w" ) as csvfile:
    fieldnames = ["Student ID", "Name", "Course", "Grade"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for student in students:
        writer.writerow({
            "Student ID": student.student_id,
            "Name": student.name,
            "Course": student.course,
            "Grade": student.grade
        })

with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

    

        