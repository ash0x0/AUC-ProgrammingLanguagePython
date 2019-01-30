import random
import sys

"""The naming and style conventions in this module break some cardinal python rules"""


def oneRun(range):
    old = -1
    counter = 0
    while True:
        i = random.randint(0, range)
        counter += 1
        if i == old:
            return counter
        old = i


def main():
    if len(sys.argv) == 2:
        while True:
            try:
                print("Number of iterations it took to find two consecutive values:", oneRun(int(sys.argv[1])))
                break
            except ValueError:
                print("Invalid input. Try again.")
    else:
        print("Using default value for range of 10")
        print("Number of iterations it took to find two consecutive values:", oneRun(10))


if __name__ == "__main__":
    main()
