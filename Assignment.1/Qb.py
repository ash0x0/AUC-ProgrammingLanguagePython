"""This module receives three integers from the user and prints all numbers divisible by the second input
in the range from first to third input"""

try:
    # Attempt to get input and cast to proper numeric type integer
    lower = int(input("Lower bound (inclusive): "))
    upper = int(input("Upper bound (inclusive): "))
    divider = int(input("Divider: "))
except ValueError:
    # If cast fails print error message and exit with error code
    print("Invalid input.")
    exit(1)
# If no error happened with the cast loop over the range and print divisible numbers
for i in range(lower, upper + 1):
    if i % divider == 0:
        print(i)
