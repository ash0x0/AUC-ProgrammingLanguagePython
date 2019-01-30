"""This number receives numeric input from the user and prints a calculated tax depending on the input"""

try:
    # Attempt to get input and cast to proper numeric type float
    x = float(input("Salary: "))
except ValueError:
    # If cast fails print error message and exit with error code
    print("Invalid input.")
    exit(1)
# If input is correct calculate and print the tax for the two possible ranges
if x < 50000:
    print("Tax:", x * 0.15)
elif x >= 50000:
    print("Tax:", x * 0.25)
