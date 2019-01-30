"""This module received three numbers from the user, computes their sum and prints the sum to the screen"""

try:
    # Attempt to get input and cast to proper numeric type float
    x = float(input("First number: "))
    y = float(input("Second number: "))
    z = float(input("Third number: "))
except ValueError:
    # If cast fails print error message and exit with error code
    print("Invalid input.")
    exit(1)
# If nothing went wrong with input casting, sum and print
print("Sum is", x + y + z)
