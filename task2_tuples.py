# Task 2: Tuples in Python

# 1. Creating a tuple
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
print("Original Tuple:", fruits)

# 2. Accessing elements using indexing
print("First Element:", fruits[0])
print("Third Element:", fruits[2])
print("Last Element:", fruits[-1])

# 3. Tuple slicing
print("First Three Elements:", fruits[0:3])
print("Elements from Index 2:", fruits[2:])
print("Tuple in Reverse Order:", fruits[::-1])

# 4. Finding the length of a tuple
print("Length of Tuple:", len(fruits))

# 5. Basic tuple operations

# Concatenation
more_fruits = ("Pineapple", "Watermelon")
combined = fruits + more_fruits
print("After Concatenation:", combined)

# Repetition
repeated = ("Apple", "Banana") * 2
print("After Repetition:", repeated)

# Membership testing
print("Is Mango in the Tuple?", "Mango" in fruits)
print("Is Kiwi in the Tuple?", "Kiwi" in fruits)

# Finding the count of an element
numbers = (10, 20, 10, 30, 10, 40)
print("Count of 10:", numbers.count(10))

# Finding the index of an element
print("Index of Mango:", fruits.index("Mango"))
