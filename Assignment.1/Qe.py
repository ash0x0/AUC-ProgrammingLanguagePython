"""This module receives two numeric inputs from the user and prints the larger of the two"""

try:
    # Attempt to get input and cast to proper numeric type float
    x = float(input("First number: "))
    y = float(input("Second number: "))
except ValueError:
    # If cast fails print error message and exit with error code
    print("Invalid input")
    exit(1)
# If input is correct print the larger number
if x > y:
    print(x)
else:
    print(y)
