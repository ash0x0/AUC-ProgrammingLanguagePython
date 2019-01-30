import re


def check_password(password):
    if not (6 < len(password) < 12):
        return False

    if (re.search('[a-z]+', password) is not None) and (re.search('[A-Z]+', password) is not None) \
            and (re.search('[0-9]+', password) is not None) and (re.search('[$#@]+', password) is not None):
                    return True
    else:
        return False


def main():
    """Test string: ABd1234@1,a F1#,2w3E,2We3345"""
    # get the input into a comma separated list
    lst = "ABd1234@1,a F1#,2w3E,2We3345".split(',')
    # placeholder for the output
    result = str()
    # iterate over the comma separated list
    for i in lst:
        # call the function that checks the password
        if check_password(i):
            # if the password is valid add it to output with a comma separator
            result += i + ','
    # print the result of the password sequence without the trailing comma
    print(result[0:-1])


if __name__ == '__main__':
    main()
