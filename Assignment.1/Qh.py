import re

"""This module receives a single formatted phone number input from the user, evaluates if it conforms to 
the proper format and if so prints the area code portion of the phone number"""


def check_number(number):
    # Check if number conforms to phone number format and return the logical value of the check
    if re.match(r'\(\d{3}\)\d{3}-\d{4}', number) is not None:
        return True
    else:
        return False


# This value is simply to keep track of the number of trials
counter = 0
# Loop until number of trials is exhausted
while counter < 2:
    # receive user input
    x = input("Phone number: ")
    # If the input is properly formatted prints the area code portion and exits
    if check_number(x):
        print("Area code is", x[1:4])
        # This is needless, simply indicates for readability the program exits here, a break could do the same
        exit(0)
    # If the input is improperly formatted, increase the trial counter and print the proper error message
    else:
        counter += 1
        if counter == 1:
            print("Invalid number. You get one more try.")
        else:
            print("Invalid input. Ran out of tries, exiting...")
