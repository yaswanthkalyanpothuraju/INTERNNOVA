n = int(input("Enter a number N: "))

# 1. Print numbers from 1 to N using a for loop
print("Numbers from 1 to", n, "using for loop:")
for i in range(1, n + 1):
    print(i, end=" ")
    
print()

# 2. Print numbers from N to 1 using a while loop
print("Numbers from", n, "to 1 using while loop:")
i = n
while i >= 1:
    print(i, end=" ")
    i -= 1

print()

# 3. Print the multiplication table
print("Multiplication table of", n, ":")
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
