
#In Python, variables are not specifically created using a variable declaration. Instead, they are created automatically when they are assigned an object reference.
#The following code segment creates three variables
def varibaleDeclarations():
    name = "John Smith"
    idNum = 42
    avg = 3.45
    print (name,idNum,avg)


def varibaleAssignments():
    name = "John Smith"
    idNum = 42
    #Python uses a single equal sign (=) for assigning an object reference to a variable. When an assignment statement is used, the reference of the object on the
    #right-hand side is copied and stored in the variable on the left hand side, not the data.
    #
    #When a new reference is assigned to an existing variable, the old reference is replaced.
    idNum = 70
    print (idNum)

    #An existing variable can be assigned a reference of any type. Thus, no type checking is performed when an assignment operation is performed. In the following code segment, the idNum variable is assigned a string instead of an integer
    idNum = "smith"
    print (idNum)

    #When one variable is assigned to another
    student = name
    print (student)

#Python does not support constant variables. Instead, it is common practice for the programmer to specify constant variables as those named with all capital letters. To create the two constant variables, you should write
#It is important to note, however, there is no way to enforce the concept of a constant variable and keep its value from being changed. By following the standard 
#convention, however, you provide information to yourself and others that you intend for a variable in all caps to be constant throughout the program.
def constants():
    TAX_RATE = 0.06
    MAX_SIZE = 100
    print (TAX_RATE, MAX_SIZE)

#call functions
varibaleDeclarations()
varibaleAssignments()
constants()