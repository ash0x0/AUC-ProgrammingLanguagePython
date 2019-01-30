"""This module receives two numeric inputs from the user, swaps them and prints the result"""

try:
    # Attempt to get input and cast to proper numeric type float
    x = float(input("First number: "))
    y = float(input("Second number: "))
except ValueError:
    # If cast fails print error message and exit with error code
    print("Invalid input")
    exit(1)
# Swap the two inputs using a third memory location referenced by z
z = x
x = y
y = z
# Print swapped numbers
print("First number:", x)
print("Second number:", y)
