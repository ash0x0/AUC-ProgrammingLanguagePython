"""This module receives a string input from the user and counts the a, b, c and other characters
and prints the count of each"""

# receive user input string
x = input("Input string: ")
# initialize the counters
a_count, b_count, c_count, other_count = 0, 0, 0, 0
# iterate over the string characters
for s in x:
    # increment the proper character counter
    if s is 'a':
        a_count += 1
    elif s is 'b':
        b_count += 1
    elif s is 'c':
        c_count += 1
    else:
        other_count += 1
# print the final count for each character category
print("a count is", str(a_count), ", b count is", str(b_count), ", others count is", str(other_count))
