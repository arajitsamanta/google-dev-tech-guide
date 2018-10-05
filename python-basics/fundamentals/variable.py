
# In Python, variables are not specifically created using a variable declaration. Instead, they are created automatically when they are assigned an object reference.
# The following code segment creates three variables


def varibaleDeclarations():
    name = "John Smith"
    idNum = 42
    avg = 3.45
    print (name, idNum, avg)


def varibaleAssignments():
    name = "John Smith"
    idNum = 42
    # Python uses a single equal sign (=) for assigning an object reference to a variable. When an assignment statement is used, the reference of the object on the
    # right-hand side is copied and stored in the variable on the left hand side, not the data.
    #
    # When a new reference is assigned to an existing variable, the old reference is replaced.
    idNum = 70
    print (idNum)

    # An existing variable can be assigned a reference of any type. Thus, no type checking is performed when an assignment operation is performed. In the following code segment, the idNum variable is assigned a string instead of an integer
    idNum = "smith"
    print (idNum)

    # When one variable is assigned to another
    student = name
    print (student)

# Python does not support constant variables. Instead, it is common practice for the programmer to specify constant variables as those named with all capital letters. To create the two constant variables, you should write
# It is important to note, however, there is no way to enforce the concept of a constant variable and keep its value from being changed. By following the standard
# convention, however, you provide information to yourself and others that you intend for a variable in all caps to be constant throughout the program.


def constants():
    TAX_RATE = 0.06
    MAX_SIZE = 100
    print (TAX_RATE, MAX_SIZE)


# ***** Varibale Scope *****
"""
built-in
    Variables and literal values defined as part of the language. These can be used anywhere within a program.
global or module
    Variables created at the top-level of a source file or module (outside of all functions and classes). Unlike other languages in which a global variable can be used anywhere within a program, each module in Python creates its own global scope.
local
    Variables created within a function are local to that function. Function and method arguments are local variables.
instance
    Variables defined as data fields of a class.    
"""
# ***** Referencing Global Variables *****
# GLobal variable declaration on module file level
varA = 40


def one(varB):
    # Access global variable varA
    varC = varA + varB
    return varC


print("Accessing global vars", varA, one(20))


def two(varB):
    # To modify a global variable from within a function, you must use the global declaration which tells the Python interpreter to modify the global variable when it is assigned a new value instead of creating a new local variable.
    global varA
    varC = varA + varB
    # Below code wont wont create a new local variable instead it will refer globally declared varA
    varA = 0
    return varC


print("Modify global vars", varA, two(20))

# call functions
varibaleDeclarations()
varibaleAssignments()
constants()
