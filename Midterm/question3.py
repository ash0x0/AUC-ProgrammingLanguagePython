def get_combinations(dictionary):
    output = []
    # iterate over the dictionary values, this is the first part cursor
    for i in dictionary.values():
        # iterate over the rest of the dictionary
        for j in dictionary.values():
            # ensure we don't use the same object with both cursors
            if i is j:
                continue
            # iterate over the elements in the list under the first cursor.
            # this could've been an improved for but I don't like python's hyper-improved for.
            for k in i:
                # iterate over the elements in the list under the second cursor
                for m in j:
                    # ensure combination uniqueness
                    if k+m not in output and m+k not in output:
                        # add the new unique combination to the container
                        output.append(k + m)
    # return the container of combinations
    return output


# test case
test = {'1':['a','b'], '2':['c','d']}
# call the function
result = get_combinations(test)
# format the output same way it's expected
for i in result:
    print(i)
