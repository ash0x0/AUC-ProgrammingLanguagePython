class Robot:

    def __init__(self, x=0, y=0):
        self.x_coordinate = x
        self.y_coordinate = y
        # this is the list of moves
        self.moves = []

    def __eq__(self, other):
        # make sure we're only comparing robots
        if not isinstance(other, Robot):
            print("Invalid comparison, can only compare two Robot objects.")
            return False
        else:
            # now we're comparing robots
            # if the lists are equal return True, otherwise False
            # Python's container equality is in serious need of work, took half an hour to make sure this behaves
            if other.moves == self.moves:
                return True
            else:
                return False

    def moveUp(self, displacement):
        # add the displacement over positive y-axis
        self.y_coordinate += displacement
        # add the number of moves with their code to the moves list
        # the reason for this loop and not concatenation is so each move is separated into its own entry
        for i in range(0, displacement):
            self.moves.append('U')

    def moveDown(self, displacement):
        # add the displacement over negative y-axis
        self.y_coordinate -= displacement
        # add the number of moves with their code to the moves list
        self.moves.append(displacement*'D')

    def moveRight(self, displacement):
        # add the displacement over positive x-axis
        self.x_coordinate += displacement
        # add the number of moves with their code to the moves list
        self.moves.append(displacement*'R')

    def moveLeft(self, displacement):
        # add the displacement over negative x-axis
        self.x_coordinate -= displacement
        # add the number of moves with their code to the moves list
        self.moves.append(displacement*'L')

    def printLocation(self):
        print("X:", self.x_coordinate, ", Y:", self.y_coordinate)


def main():
    """This is all just testing"""
    first = Robot(2, 3)
    first.printLocation()
    first.moveUp(3)
    first.printLocation()
    first.moveRight(3)
    first.printLocation()
    first.moveDown(3)
    first.printLocation()
    first.moveLeft(3)
    # create a second robot for comparison, this robot has different moves
    second = Robot(5, 8)
    second.moveUp(2)
    second.moveRight(4)
    second.moveDown(6)
    second.moveLeft(7)
    # the two robots shouldn't be equal, this should be false
    print(second == first)
    # create a third robot for comparison, it has the same moves as first
    third = Robot(5, 7)
    third.moveUp(3)
    third.moveRight(3)
    third.moveDown(3)
    third.moveLeft(3)
    # these two are equal, this should be true
    print(third == first)


if __name__ == '__main__':
    main()
