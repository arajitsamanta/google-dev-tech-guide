
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

# Python provides several means for deleting items from a list. The first approach uses the remove() method which allows you to 
# delete an item by value.
def removeItems():
    theList = [ 10, 11, 12, 13 ]

    # Delete an item
    # Function prototype -> list.remove(item)
    theList.remove(11)
    print("After removing list is",theList)

    # To remove an item by index, you can use the pop() method which retrieves and then removes the item at the given index. 
    # In the following code segment, we use the pop() method to retrieve and remove the item at index position one.
    # When an item is removed from the list, the items in sequential order following the removed item are shifted down and the 
    # size of the list shrinks by one. You can omit the index position for pop() and the item in the last element will be retrieve and removed.
    # Function prototype -> list.pop(index=0)
    x=theList.pop()
    print("Remove a list item using index", theList,", Removed item is",x)

def listSearch():

    # **** Item Search ****
    # We can search for an item within the list using the index() method which returns the element index of the first occurrence in
    # the list of the given value. If the list does not contain the given value, an exception is raised.
    #Function prototype -> list.index(item)
    theList = [ 10, 11, 12, 12, 13 ]
    pos = theList.index( 13 )
    print("Index of deleted item is",pos) 

    # **** Membership ****
    # As with strings, the in operator (and the not in version) can be used to determine if the list contains a given item.
    # Function prototype -> item in list
    if 13 in theList:
        print("13 am an existing item in the list")

    # use list.index() in conjunction with in to find out index of an item.
    if 12 in theList:
        print("12 exists at index",theList.index(12))
    else:
        print("12 don't exists")

    # To count no of occurences of a particular item in the list, we can use count() method
    # Function prototype -> list.count(item)
    print("12 exists",theList.count(12) , "times in the list")

    # **** Min and Max of a List ****
    # To find min and max of a numeric list we can use min() and max() function
    # Function prototype -> min(), max()
    print("Min ",min(theList), "Max", max(theList))

# Invoke test functions
addListItems()
orderedList()
removeItems()
listSearch()