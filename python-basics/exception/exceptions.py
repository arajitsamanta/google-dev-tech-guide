
def catchingException():
    # In python exception can be handled by using try.. exception block
    try:
        myList = [12, 50, 5, 17]
        print(myList[4])
    except IndexError:
        print("Error: Index out of range.")

    # Multiple except block
    try:
        x = 0
        myList = [12, 50, 5, 17]
        print(myList[3] / x)
    except IndexError:
        print("Error: Index out of range.")
    except ZeroDivisionError:
        print("Error: Attempt to divide by zero.")
    except:
        print("Error: An exception was raised.")


def average(valueList):
    # Python also defines the assert statement which can be used to make assertions within your program. This is very useful for debugging programs.
    assert len(valueList) > 0, "Empty list in average()."
    total = 0
    for x in valueList:
        total = total + x

    try:
        avg = total / len(valueList)
        return avg

    except ZeroDivisionError:
        return 0.0


def raiseException(value1, value2):
    if value1 == None or value2 == None:
        # You can also raise an exception within your program
        raise TypeError
    if value1 < value2:
        return value1
    else:
        return value2


# Invoke functions
catchingException()

# Handlers at Different Scopes
# The try blocks can be used at any position within a program. When an exception is raised, it is passed up to an earlier try block if it is not handled by a local try block.
myList = [12, 50, 5, None, 17]
try:
    listAvg = average(myList)
    print("The average = ", listAvg)

except TypeError:
    print("An invalid type was in the list.")
# Raise exception
try:
    raiseException(None, 2)
except TypeError:
    print("Raised exception")
