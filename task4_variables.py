# Global variable
x = 100

def show_variables():
    # Local variable
    y = 50

    print("Local variable y =", y)
    print("Global variable x =", x)

# Calling the function
show_variables()

# Accessing the global variable outside the function
print("Global variable outside function x =", x)

# Trying to access the local variable outside the function
try:
    print(y)
except NameError:
    print("Local variable y cannot be accessed outside the function.")
