# class person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name  
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

# class Student(person):
#     def __init__(self, first_name, last_name, year):
#         super().__init__(first_name, last_name)  
#         self.graduation_year = year
#     def welcome(self):
#         print(f"Welcome {self.full_name()} to the class of {self.graduation_year}")
# class schoolinformation:
#     def __init__(self, school_name):
#         self.school_name = school_name
# class student(person,schoolinformation):
#     def __init__(self, first_name, last_name, year, school_name):
#         person.__init__(self, first_name, last_name)  
#         schoolinformation.__init__(self, school_name)
#         self.graduation_year = year
#     def welcome(self):
#         print(f"Welcome {self.full_name()} to {self.school_name} class of {self.graduation_year}")
# student1 = student("john", "Jaffri", 2025, "QBHSS")
# student1.welcome()


class person:
    def __init__(self,name):
        self.name=name

class student(person):
    def study(self):
        print(self.name , "Is Studying")
    def role(self):
        print("Attend The Class")

class Teacher(person):
    def teach(self):
        print(self.name , " Is Teaching ")
    def role(self):
        print("Teach The Student")

class monitor(student , Teacher):
    def monitor(self):
        print(self.name , " Is Manging Student ")


def describe_role(obj):
    obj.role()
describe_role(student("Hussain"))
describe_role(Teacher("Hussain"))