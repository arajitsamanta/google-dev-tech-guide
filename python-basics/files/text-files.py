
def fileOperations() :
    #Opening file - open() returns a file object, and is most commonly used with two arguments
    #Function prototype -> open(filename, mode)
    infile = open( 'records.txt', 'r' )

    #Reading a File
    line = infile.readline()
    while line!="":
        print(line)
        line=infile.readline()

     #closing a file
    infile.close()

    #Read a single character
    infile = open( 'records.txt', 'r' )
    ch = infile.readline(1)
    print(ch)
    infile.close()

    #Read multi lines
    infile = open( 'records.txt', 'r' )
    lines = infile.readlines()
    print(lines)
    infile.close()

    #Read a file using iterator
    fileItr = open( 'records.txt', 'r' )
    for line in fileItr:
        #rstrip() strip new line character from the end of line and return it.In case of no new line, it does nothing.
        print(line.rstrip())
    fileItr.close

    #To extract mixed type data stored on the same input line, we must first split or tokenize the string into individual parts using the split()
    #method of the string class.
    aString = "12 45.5 abc 9"
    strList = aString.split()
    print(strList)

    #The split() method splits or tokenizes a string into substrings and stores the results in a string list. By default, the string is split using whitespace 
    #characters as the delimiter. You can also specific a set of delimiters as a argument.
    ssn = "412-45-8900"
    parts = ssn.split( "-" )
    print(parts)

    #Writting to a file
    outfile = open('new-file.txt','w')
    outfile.write("another line 20")
    outfile.close()

#Invoke test functions
fileOperations()