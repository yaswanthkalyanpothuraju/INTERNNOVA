# Week 5 - Task 1: Classes and Objects
# Project: Student Information System

# Creating a Student class
class Student:

    # Method to display student information
    def display_info(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("--------------------------")


# Creating the first object
student1 = Student()

# Assigning attributes to the first object
student1.student_id = 101
student1.name = "Rahul"
student1.age = 21
student1.course = "Artificial Intelligence"

# Creating the second object
student2 = Student()

# Assigning attributes to the second object
student2.student_id = 102
student2.name = "Kalyan"
student2.age = 22
student2.course = "Data Science"

# Displaying student information
print("STUDENT MANAGEMENT SYSTEM")
print("==========================")

print("\nFirst Student Details:")
student1.display_info()

print("Second Student Details:")
student2.display_info()