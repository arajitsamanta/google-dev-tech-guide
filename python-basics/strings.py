
def stringExample():
    # creates an object storing the given literal string and its reference is assigned to name. 
    name = "John Smith" 
    # You can also create a string using the str() constructor
    student = str("john doe")
    print(name, student)

    # The string constructor can also be used to create string representations of numeric and boolean values.
    x = 45
    intStr = str( x )          # '45'
    floatStr = str( 56.89 )    # '56.89' 
    boolStr = str( False )     # 'False'
    print(intStr,floatStr,boolStr)

    # Likewise, the numeric type constructors can be used to convert numeric strings to the respective type. An exception is 
    # raised if the string does not contain a valid literal numeric value.
    i = int( "85" )      # 85
    f = float( '3.14' )  # 3.14
    print(i,f)

    multilineString="""This is a string which
      can continue onto a new line. When printed, it will appear
        exactly as written between the trip quotes."""
    print(multilineString)

# The common escape sequences are shown in the following table
#
#   Sequence	Description
#   ==========================
#   \\	Backslash (produces \)
#   \'	Single quote (produces ')
#   \"	Double quote (produces ")
#   \n	Newline (produces a newline)
#   \t	Horizontal tab
def escapeSequence():
    msg = "Start a newline here.\nusing the \\n character."
    print(msg)

#Invoke test functions
stringExample()
escapeSequence()