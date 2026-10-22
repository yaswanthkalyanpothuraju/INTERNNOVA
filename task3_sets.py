# Task 3: Sets in Python
# 1. Creating a set
fruits = {"Apple", "Banana", "Mango", "Orange"}
print("Original Set:", fruits)

# 2. Removing duplicate values
numbers = {10, 20, 10, 30, 20, 40, 30}
print("Set after Removing Duplicates:", numbers)

# 3. Adding elements
fruits.add("Grapes")
print("After Adding an Element:", fruits)

# Adding multiple elements
fruits.update(["Pineapple", "Watermelon"])
print("After Adding Multiple Elements:", fruits)

# 4. Removing elements
fruits.remove("Banana")
print("After Removing Banana:", fruits)

# Using discard() to remove an element safely
fruits.discard("Kiwi")
print("After Using Discard:", fruits)

# 5. Union of sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", set_a.union(set_b))

# 6. Intersection of sets
print("Intersection:", set_a.intersection(set_b))

# 7. Difference of sets
print("Difference (A - B):", set_a.difference(set_b))
print("Difference (B - A):", set_b.difference(set_a))