def common(first_list, second_list):
    """Receives two lists, returns True if they have any common objects and false otherwise.
    Note that this implementation should theoretically work with any container-like object for which
    the in operator doesn't have a different meaning."""
    # iterate over the elements in the first list
    for i in first_list:
        # if the current element in the second list, short-circuit and return True
        # one common object satisfies "at least one"
        if i in second_list:
            return True
    # fall through to False
    return False


# get first input list
first = input("Enter the first list, elements separated by commas no need for anything else:").split(",")
# get second input list
second = input("Enter the second list in the same format:").split(",")
# print the result of common() on the two lists
print(common(first, second))
