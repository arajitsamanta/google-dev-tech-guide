
# **** ListBasics *****
# Python does not provide the simple array type like that found in Java and other languages. Instead, it provides the built-in list type which is a dynamic
# array similar to a Vector in Java. The Python list defines a positional ordering from left to right like an array, but its size can change during execution as
# items are added and deleted.


def listbasics():
    # create list
    gradeList = [85, 90, 87, 65, 91]
    print(gradeList)

    # List element access - List elements are referenced using the square bracket subscript notation, the same as in Java. The elements are numbered in sequential
    # order, with the first element having index zero.
    print("Forward:", gradeList[0], gradeList[3])
    print("Reverse:", gradeList[-1], gradeList[-3])

    # List length can be obtained by using built-in len() function.
    print("The list contains %d elements." % len(gradeList))

# **** Simulating an array *****


def simulateArray():
    # Python lists are variable length, however, and can change size during the execution of the program. There is no equivalent command to create a fixed size list.
    # But we can simulate a Java array be creating a list with a preset number of elements. Python defines the repeat operator (*) for use with lists. The following
    # statement
    histogram = [0] * 10

    gradeList = [85, 90, 87, 65, 91]

    # Count the number of each grade.
    i = 0
    length = len(gradeList)
    while i < length:
        grade = gradeList[i] // 10
        histogram[grade] += 1
        i += 1

    # Return the histogram.
    return histogram


def listIteration(valueList):
    total = 0
    for value in valueList:
        total = total + value
    avg = float(total) / len(valueList)
    print("The average value = %6.2f" % avg)

# ***** Tuples *****
# Another built-in type for creating an indexed collection of objects is the tuple. Tuples are exactly like lists, except they are immutable. A tuple is created using
# a pair of parentheses instead of square brackets.


def tuples():
    t = (0, 2, 4)           # 3 element tuple
    a = (2, )                # 1 element tuple
    b = ('abc', 1, 4.5, 5)  # 4 element mixed tuple
    c = (0, ('a', 'b'))   # nested tuple
    print(t, a, b, c)

    # When multiple values are passed as data fields in a formatted string, those values are listed within parentheses.That is actually a tuple.
    print("(%d, %d)" % (4, 5))


# Invoke test functions
listbasics()
print(simulateArray())
listIteration([2, 3, 4, 5, 6])
tuples()
