def main():
    # this loop is for the purpose of retrying should the input string format isn't a valid arithmetic expression
    while True:
        # placeholder for the input string
        txt = ""
        # this loop is for retrying if the input string has anything other than 'a' or '+'
        while True:
            # get the input
            txt = input("Input the string to evaluate:")
            # this flag marks when to break from the outer loop
            flag = False
            # loop over te characters of the input
            for i in txt:
                # if character is other than 'a' or '+' print invalid message and set flag to continue outer loop
                if i != '+' and i != 'a':
                    print("Invalid input. Only characters 'a' and '+' are accepted.")
                    flag = True
                    break
            # continue the outer loop if the flag is set, otherwise break with the accepted input
            if not flag:
                break
        # this loop does retrying for number input in case it isn't a number
        while True:
            # get input and try to cast it to a number, if not possible print error and retry
            try:
                number = int(input("Input the number to replace with:"))
                # if the preceding statement succeeds without exception then we have a valid digit
                break
            except ValueError:
                print("This is not a number, only integers are accepted.")
        # replace the character 'a' with the chosen digit
        txt = txt.replace('a', str(number))
        # evaluate the expression, it the eval fails then the expression isn't valid arithmetic
        try:
            print(eval(txt))
            # if the eval doesn't produce an error break from the outermost retry loop
            break
        except:
            # print an error message and keep the loop going
            print("The input string format isn't a valid numerical operation.")


if __name__ == '__main__':
    main()
