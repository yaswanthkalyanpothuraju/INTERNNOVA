# Task 1: Lists in Python
# 1. Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Original List:", fruits)

# 2. Accessing elements
print("First Element:", fruits[0])
print("Third Element:", fruits[2])

# 3. Adding elements
fruits.append("Grapes")
print("After Adding an Element:", fruits)

# Adding an element at a specific position
fruits.insert(1, "Pineapple")
print("After Inserting an Element:", fruits)

# 4. Updating elements
fruits[2] = "Watermelon"
print("After Updating an Element:", fruits)

# 5. Removing elements
fruits.remove("Mango")
print("After Removing Mango:", fruits)

# Removing the last element
fruits.pop()
print("After Removing Last Element:", fruits)

# 6. Sorting the list
fruits.sort()
print("Sorted List:", fruits)