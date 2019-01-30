"""This module receives a single numeric input from the user, calculates if summation of the digits of the input is
divisible by 7 and informs the user of the result"""

# receive user input
x = input("Number: ")
# initialize summation to 0
summation = 0
# loop over the number's digits and add each digit value to the summation
for s in x:
    if s.isnumeric():
        summation += int(s)
# If summation is not its initial value and divisible by 7 inform the user the digits sum is divisible by 7
if summation != 0 and summation % 7 == 0:
    print("Sum of the digits is divisible by 7")
else:
    print("Sum of the digits isn't divisible by 7")
