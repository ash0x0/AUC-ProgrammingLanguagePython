def main():
    print("Start inputting the sequence, will stop taking input if an empty line is encountered:")
    # loop to get the input
    while True:
        # get input and insert to the lines list
        line = input(">>>>")
        # if the last input line is empty inform the user and break from input loop
        if line == "":
            break
        placeholder = ""
        # loop over the current words in the line, separated by space, this will not work if proper punctuation
        # isn't followed, for example "hello,world" isn't proper, it should be "hello, world" with a preceding space
        for i in line.split(' '):
            # capitalize the current word and add it to the line placeholder with a succeeding space
            placeholder += i.capitalize() + ' '
        # print the line after removing the trailing space to the list of resulting lines
        print(placeholder[:-1])


if __name__ == '__main__':
    main()
