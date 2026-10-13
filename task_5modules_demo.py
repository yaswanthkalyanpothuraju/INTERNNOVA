
# Import built-in modules
import math
import random
import datetime

# 1. Math module - Calculate square root
number = float(input("Enter a number to find its square root: "))

if number >= 0:
    result = math.sqrt(number)
    print("Square root of", number, "is", result)
else:
    print("Square root of a negative number is not a real number.")

# 2. Random module - Generate a random number
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

# 3. Datetime module - Display current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime.strftime("%d-%m-%Y %H:%M:%S"))
