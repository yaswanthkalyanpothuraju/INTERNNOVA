
# Week 5 - Task 3: Inheritance
# Project: Student Information System

# Parent Class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Common method inherited by child class
    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class inheriting Person
class Student(Person):

    def __init__(self, name, age, student_id, course):
        # Calling parent class constructor
        super().__init__(name, age)

        self.student_id = student_id
        self.course = course

    # Child-specific method
    def display_student(self):
        print("\n--- Student Details ---")

        # Inherited method
        self.display_person()

        # Child class attributes
        print("Student ID:", self.student_id)
        print("Course:", self.course)


# Creating Student objects
student1 = Student("Rahul", 21, 101, "Artificial Intelligence")

student2 = Student("Kalyan", 22, 102, "Data Science")


# Displaying student information
print("STUDENT INHERITANCE PROGRAM")

student1.display_student()
student2.display_student()