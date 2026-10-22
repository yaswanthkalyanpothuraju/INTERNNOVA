# Student Information Dictionary

# 1. Creating a student information dictionary
student = {
    "Name": "Yaswanth",
    "Age": 21,
    "Course": "AI & DS",
    "City": "Vinukonda"
}

print("Original Student Information:")
print(student)

# 2. Accessing values
print("\nAccessing Student Details:")
print("Name:", student["Name"])
print("Age:", student["Age"])
print("Course:", student["Course"])
print("City:", student["City"])

# Using get() method
print("Student Name using get():", student.get("Name"))

# 3. Adding new key-value pairs
student["College"] = "Dhanalakshmi Srinivasan University"
student["Year"] = "Final Year"

print("\nAfter Adding New Details:")
print(student)

# 4. Updating values
student["Age"] = 22
student["City"] = "Chennai"

print("\nAfter Updating Details:")
print(student)

# 5. Removing data
student.pop("Year")
print("\nAfter Removing Year:")
print(student)

# Removing a key using del
del student["College"]
print("\nAfter Removing College:")
print(student)

# 6. Displaying keys and values
print("\nAll Keys:")
print(student.keys())

print("\nAll Values:")
print(student.values())

print("\nAll Key-Value Pairs:")
print(student.items())

# 7. Using dictionary methods

# update() method
student.update({"Age": 21, "City": "Vinukonda"})
print("\nAfter Using update():")
print(student)

# setdefault() method
student.setdefault("Email", "student@example.com")
print("\nAfter Using setdefault():")
print(student)

# copy() method
student_copy = student.copy()
print("\nCopied Student Dictionary:")
print(student_copy)

# len() method
print("\nTotal Number of Details:", len(student))

# clear() method demonstration on a separate dictionary
temp = {"Subject": "Python"}
temp.clear()
print("\nDictionary After clear():", temp)
