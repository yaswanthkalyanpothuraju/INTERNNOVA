# Week 5 - Task 2: Constructors
# Project: Student Information System

# Creating Student class
class Student:

    # Constructor to initialize object attributes
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    # Method to display student information
    def display_info(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("--------------------------")


# Creating objects with different values
student1 = Student(101, "Rahul", 21, "Artificial Intelligence")

student2 = Student(102, "Kalyan", 22, "Data Science")

# Displaying initialized attributes
print("STUDENT INFORMATION SYSTEM")
print("==========================")

print("\nFirst Student Details:")
student1.display_info()

print("Second Student Details:")
student2.display_info()