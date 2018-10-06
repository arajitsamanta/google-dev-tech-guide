# point.py
# Defines a class to represent two-dimensional discrete points.


class Point:

    # Python default constructor
    # Instance variables are specified by preceding the name with the self reference. Even though a data field can be defined within any method, common practice
    # dictates that data fields should be defined within the constructor. The Point class defines two data fields in the constructor, xCoord and yCoord,
    def __init__(self, x=0, y=0):
        self.XCoord = x
        self.YCoord = y

    # Class methods of the form __xyz__() are actually operator definitions and can not be called directly. Instead, they are called automatically for
    # the appropriate operator. In our example above, the __init__() method is automatically called when creating an object and the __str__() method is
    # automatically called when converting the object to a string.
    def __str__(self):
        return "(" + str(self.XCoord) + ", " + str(self.YCoord) + ")"

    def getX(self):
        return self.XCoord

    def getY(self):
        return self.YCoord

    def shift(self, xInc, yInc):
        self.XCoord += xInc
        self.YCoord += yInc
