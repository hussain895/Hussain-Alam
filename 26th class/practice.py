from abc import ABC, abstractmethod

class CourseseBase(ABC):
    @abstractmethod
    def enroll_student(self,student_name):
        pass
    def drop_student(self,student_name):
        pass
    def display_course(self):
        pass

class Course(CourseseBase):
    def __init__(self , course_name , course_code , max_student):
        self._course_name_ = course_name
        self._course_code_ = course_code
        self._max_student_ = max_student
        self._students = []       
    def enroll_student(self,student_name):
        if len(self._students) < self._max_student_:
            self._students.append(student_name)
            print(f"{student_name} has been enrolled in {self._course_name_}.")
        else:
            print(f"Cannot enroll {student_name}. The course is full.")
    def drop_student(self,student_name):
        if student_name in self._students:
            self._students.remove(student_name)
            print(f"{student_name} has been dropped from {self._course_name_}.")
        else:
            print(f"{student_name} is not enrolled in {self._course_name_}.")
    def display_course(self):
        print(f"Course Name: {self._course_name_}")
        print(f"Course Code: {self._course_code_}")
        print(f"Max Students: {self._max_student_}")
        print("Enrolled Students:")
        for student in self._students:
            print(f"- {student}")