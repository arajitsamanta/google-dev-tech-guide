
def stringExample():
    #creates an object storing the given literal string and its reference is assigned to name. 
    name = "John Smith" 
    #You can also create a string using the str() constructor
    student = str("john doe")
    print(name, student)

    #The string constructor can also be used to create string representations of numeric and boolean values.
    x = 45
    intStr = str( x )          #'45'
    floatStr = str( 56.89 )    #'56.89' 
    boolStr = str( False )     #'False'
    print(intStr,floatStr,boolStr)

    #Likewise, the numeric type constructors can be used to convert numeric strings to the respective type. An exception is 
    #raised if the string does not contain a valid literal numeric value.
    i = int( "85" )      #85
    f = float( '3.14' )  #3.14
    print(i,f)

    multilineString="""This is a string which
      can continue onto a new line. When printed, it will appear
        exactly as written between the trip quotes."""
    print(multilineString)

#The common escape sequences are shown in the following table
#
#  Sequence	Description
#  ==========================
#  \\	Backslash (produces \)
#  \'	Single quote (produces ')
#  \"	Double quote (produces ")
#  \n	Newline (produces a newline)
#  \t	Horizontal tab
def escapeSequence():
    msg = "Start a newline here.\nusing the \\n character."
    print(msg)

def stringOperations():
    ##String concatenation
    strvar = 'This is '
    fullstr = strvar + "a string"
    print('String concatenation using +', fullstr)

    #In case if any other type other than string, explict conversion needed using str() function.
    result = "String concatenation using str() function, The value of x is " + str(15)
    print (result)

    #Two strings literals can also be concatenated by placing them adjacent to each other
    print("These two string literals " "will be concatenated.")

    ##String length
    #Python provides the built-in len() function that is used to get the length of a string
    print("Length of the string = ", len('john doe'))

    ##Character Access
    #In Python, we use an array subscript with the first character having an index of zero.
    msg = "This is a string!"
    print("The first character is", msg[0])
    print("The last character is", msg[len(msg)-1])

    #Python allows you to index from the end instead of the front by using negative subscripts. The last statement in th previous code segment could be rewritten as follows
    print("The last character is", msg[-1])

    ##Extracting substring.
    #Python provides the slicing operator for extracting a substring. 
    name = "John Smith"
    first = name[0:4]
    last = name[5:]
    print(first,last)
    #You can also slice a string from the end using a negative index. The following statement
    #extracts the substring 'John S' from the string name and creates a new string which is assigned to end.
    end = name[:-4]
    print(end)

    ##String duplication
    #Python provides a string operation not found in Java for duplicating or repeating a string. Printing a dashed line is a common operation in text-based 
    #applications. One way to do it is as a string literal
    print("---------------------------------------------")
    print("-" * 45)

    ##Formatted String
    #Python overloads the binary and modulus operator (%) to work with strings. When applied to a string, it creates a new formatted string similar to the printf() 
    #method in Java and the sprintf() function in C. Consider the following example
    avgGrade=5.789
    output = "The average grade = %5.2f" % avgGrade
    print(output)
    #Above can be written as
    print("The average grade = %5.2f" % avgGrade)

    """The formal description for the string format operator is shown below and consists of two parts: the format definition string and the values used to replace
    the format codes within that definition

        format-definition-string % replacement-value(s)

    If more than one format specifier is used in the format definition, the replacement values must be placed within parentheses and separated with a comma
    """
    print("Origin: (%d, %d)\n" % (3, 8))

    """ The general structure of a format specifier is

    %[flags][width][.precision]code
    where

    flags
        Used to indicate zero fills (0) which fills preceding blank spaces within the field with 0 and optional justification within the given field width: + for right-justification or - for left-justification.
    width
        An integer value indicating the number of spaces in the current field used when formatting the replacement value.
    precision
        The number of digits to be printed after the decimal place when printing a real value.
    code
        One of the format specificer codes which are the same as those found in Java
    """
    #Python format code and description
    """
        Code	Description
        %s	String (or any object)
        %c	Character (from an ASCII value)
        %d	Decimal or integer value
        %i	Integer value (same as %d)
        %u	Unsigned integer
        %o	Octal integer
        %x	Hexadecimal integer
        %X	Same as %x but uppercase
        %e	Floating-point with exponent
        %E	Same as %e but uppercase
        %f	Floating-point no exponent
        %g	Same as %e or %f
        %G	Same as %g but uppercase
        %%	Prints a literal %
    """

#Invoke test functions
stringExample()
escapeSequence()
stringOperations()