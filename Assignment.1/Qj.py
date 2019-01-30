import math

"""This module receives five numbers from the user and calculates and prints the standard deviation for their values"""

# a list to hold the references to the five inputs
numbers = []
try:
    # try to get user input, cast and add them to the input list
    numbers.append(float(input("First number: ")))
    numbers.append(float(input("Second number: ")))
    numbers.append(float(input("Third number: ")))
    numbers.append(float(input("Fourth number: ")))
    numbers.append(float(input("Fifth number: ")))
except ValueError:
    # if cast fails, print an error message and exit with error code
    print("Invalid input")
    exit(1)
# calculate the average of the numbers
avg = sum(numbers[0:]) / 5
# iterate over the numbers and replace each in the list with the squared difference of the itself and the global average
for i in range(0, len(numbers)):
    numbers[i] = math.pow(numbers[i] - avg, 2)
# initialize the summation
summation = 0
# iterate over the squared differences in the list and sum them all
for number in numbers:
    summation += number
# get the square root of the summation of squared differences i.e. the standard deviation
result = math.sqrt(summation)
# print the final result for the standard deviation
print("Standard deviation is", str(result))
