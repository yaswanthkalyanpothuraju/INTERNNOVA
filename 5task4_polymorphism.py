
# Week 5 - Task 4: Polymorphism
# Project: Employee Work Management System

# First class
class Developer:

    def work(self):
        print("Developer is writing Python code.")


# Second class
class Designer:

    def work(self):
        print("Designer is creating website designs.")


# Third class
class Tester:

    def work(self):
        print("Tester is checking software for errors.")


# Creating objects
employee1 = Developer()
employee2 = Designer()
employee3 = Tester()


# Demonstrating polymorphism
print("EMPLOYEE WORK MANAGEMENT SYSTEM")
print("--------------------------------")

employee1.work()
employee2.work()
employee3.work()

print("--------------------------------")
print("All employees completed their tasks.")
