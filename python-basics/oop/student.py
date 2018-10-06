# student.py
#
# Defines a class to represent information for an individual student.


class Student:
    "Represents an individual student."

    def __init__(self, idNum=0, classStanding=0,
                 firstName="", lastName="",
                 gpa=0.0):
        self.idNum = idNum
        self.classStanding = classStanding
        self.firstName = firstName
        self.lastName = lastName
        self.gpa = gpa

    def getClass(self):
        """Returns the string representation for the student's
               classification code."""
        if self.classStanding == 0:
            return "Freshman"
        elif self.classStanding == 1:
            return "Sophomore"
        elif self.classStanding == 2:
            return "Junior"
        else:
            return "Senior"

    def getName(self, reversed):
        """Returns the student's name in one or two formats:
           'first last' if reversed is false or 'last first'
           if reversed is true."""
        if reversed == False:
            return self.firstName + " " + self.lastName
        else:
            return self.lastName + " " + self.firstName

    def getId(self):
        return self.idNum

    def getGPA(self):
        return self.gpa


class StudentList:
    def __init__(self):
        self.theList = []

    def addStudent(self, student):
        self.theList.append(student)

    def deleteStudent(self, idNum):
        return None

    def findStudent(self, idNum):
        return None

    def findHighestGPA(self):
        return None

    def printReport(self):
        return None
