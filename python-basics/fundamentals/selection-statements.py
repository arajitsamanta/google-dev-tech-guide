
# Selections are made in Python as in Java using the if statement. Python has a boolean class to represent logical values and a complete set of logical operators.


def booleanClass():
    """
    Python provides a boolean class which defines the two values True and False for use with logical expressions. Python will implicitly convert other types to a boolean when necessary. The basic rules are

    Non-zero numeric values are converted to True while a value of zero, both integer and floating-point, is False.
    1. For all other types, the values are converted to True if the object is nonempty and False when they are empty.
    2. The built-in function bool( x ) can be used to convert value x to a boolean using these standard rules.

    An empty literal string ("") is considered empty and will evaluate to False.
    """
    x = ""
    print(bool(x))
    print(bool(1))


def logicalOperators():
    # The relational operators available in Python include
    #   <   >   <=   >=   ==   !=   <>
    if 5 < 6:
        print("5 is less than 6")

    if 5 != 6:
        print("5 is not equal to 6")

    # boolean operators - or and not
    if 5 < 6 and 5 != 6:
        print("5 is less than 6 and also not equal to 6")


def evaluationAndReference():
    # Value comparison
    x = "abc"
    y = "abc"
    if x == y:
        print("If the == operator is applied to two string variables in Python, the strings themselves are compared and not the variable references. This is the case for all Python variables since all variables are object references.")

    # Reference comparison.
    # To compare references themselves, that is the addresses stored in the variables, Python provides the is operator.
    name1 = "Smith"
    name2 = "Jones"
    print("varible reference point to different location in memory ", name1 is name2)
    name2 = name1
    print("varible reference point to same location in memory ", name1 is name2)

    # Null reference
    # The is operator along with None can tests for null references.
    result = name1 is None
    result2 = name1 == None
    print(result, result2)
    # check if a varible is null
    x = None
    print(x is None)


def ifStatements():
    # Simple If statement
    value = -4
    if value < 0:
        print("The value is negative.")

    # If-Else structure
    value = 5
    if value < 0:
        print("The value is negative.")
        value = abs(value)
    else:
        print("The value is positive.")

    # Multiway branching
    avgGrade = 4.5
    if avgGrade >= 90.0:
        letterGrade = "A"
    elif avgGrade >= 80.0:
        letterGrade = "B"
    elif avgGrade >= 70.0:
        letterGrade = "C"
    elif avgGrade >= 60.0:
        letterGrade = "D"
    else:
        letterGrade = "F"
    print(letterGrade)


def stringEvaluation():
    # The normal equivalency operator is also used in Python to evaluate strings.
    str1 = "Abc Def"
    str2 = "Abc def"
    if str1 == str2:
        print("Equal!!")
    else:
        print("Not Equal!!")

    # The lexicographical order of two strings is determined using the appropriate logical operator instead of the compareTo() operator as is done in Java
    name1 = "Smith, John"
    name2 = "Smith, Jane"
    if name1 < name2:
        print("Name1 comes first.")
    elif name1 > name2:
        print("Name2 comes first.")
    else:
        print("The names are the same.")

    # Contains
    # To determine if a string contains a substring of characters, Python provides the in operator. In the following example,
    if "Smith" in name1:
        print(name1)
    # There is also a not version of the in operator that can be used to determine if a string dose not contain a substring.
    if "Jones" not in name1:
        print("Name not found")


# Invoke test functions
booleanClass()
logicalOperators()
evaluationAndReference()
ifStatements()
stringEvaluation()
