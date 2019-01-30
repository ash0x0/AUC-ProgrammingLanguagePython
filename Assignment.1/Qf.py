"""This module receives a single number input from the user for a GPA and prints a message depending on the value"""

try:
    # Attempt to get input and cast to proper numeric type float
    x = float(input("GPA: "))
except ValueError:
    # If cast fails print error message and exit with error code
    print("Invalid input")
    exit(1)
"""Print the proper message depending on the range, if value isn't in the range print an error message 
and exit with error code"""
if 0 <= x < 1:
    print("No comment!")
elif 1 <= x < 2:
    print("Hmm!")
elif 2 <= x < 3:
    print("Good!")
elif 3 <= x <= 4:
    print("Superb!")
else:
    print("Invalid input, must be in range [0,4]")
    # The exit is needles, it is merely here to indicate an error code
    exit(1)
