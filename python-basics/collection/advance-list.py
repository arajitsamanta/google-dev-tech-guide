
import random

def addListItems():
    # Create the empty list.
    valueList = []

    # Appending Items - New items can be appended to the end of the list using the append() method.
    # Build the list of 10 random values.
    for i in range( 10 ) :
        valueList.append( random.random() )
    print("Appending to list",valueList)

    # Appending multiple items - The extend() method can be used to append multiple items to the end of a list.
    listA = [ 0, 1, 2, 3 ]
    valueList.extend(listA)
    print("Extending list",valueList)

    # Inserting items - Python defines the insert() list method for inserting items anywhere within a list.
    # list.insert( atIndex, value )
    #   atindex:
    #           This is the index where we want to insert. If atIndex is beyond the end of the list, the value is appended to the end. Negative indicies can be used 
    #           to reference a particular element from the end of the list.
    #   value:
    #           The value to be inserted. Remember, that an alias is created for the given value and inserted into the list.
    valueList.insert(1,80)
    print("Inserting anywhere in list",valueList)

# Extracts a list of integers from a text file, one per line  and creates an ordered list using the insert() method.
def orderedList():
    # Start with an empty list.
    theList = []

    theFile = open( "values.txt", "r" )
    for line in theFile:
        num = int( line )

        # Find the proper position of the item.
        i = 0
        while i < len( theList ) and num > theList[ i ]:
            i = i + 1

        # Insert the item.
        theList.insert( i, num )

    #close file
    theFile.close()
    print("Ordered list created from file",theList)

# Invoke test functions
addListItems()
orderedList()