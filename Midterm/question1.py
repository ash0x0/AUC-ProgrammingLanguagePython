# get input and split into a list
input_list = input("Enter the strings separated by commas, no need for quotes or spaces (WHITESPACE ARE STRIPPED): ")\
    .split(",")
# container for valid string count
count = 0
# iterate over the input list elements
for i in input_list:
    # strip just in case there are spaces
    i = i.strip()
    # if the element is longer than 2 and first character is the same as last count it
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1
# print the total count
print("Number of valid strings is", count)
