import sys
from OneRun import oneRun

"""The naming and style conventions in this module break some cardinal python rules"""


def Experimenter(nTimes, range):
    lst = []
    i = int()
    while i < nTimes:
        i += 1
        lst.append(oneRun(range))
    print("Maximum:", max(lst), "Minimum:", min(lst), "Average:", sum(lst)/len(lst))
    return max(lst), min(lst), sum(lst)/len(lst)


def main():
    if len(sys.argv) > 1:
        if len(sys.argv) != 3:
            print("Invalid arguments. Correct usage: python3 Experimenter.py nTimes range")
        else:
            while True:
                try:
                    print(Experimenter(int(sys.argv[1]), int(sys.argv[2])))
                    break
                except ValueError:
                    print("Invalid input, only integers accepted. Try again.")
    else:
        print("Using default values for nTimes and range of 10 and 10")
        Experimenter(10, 10)


if __name__ == "__main__":
    main()
