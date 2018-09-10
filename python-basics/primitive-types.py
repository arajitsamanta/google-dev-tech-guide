
def primitiveTypes():
    #Integers
    a=-9
    b=0x4F
    print ("Integer:",a)
    print ("Hexadecimal integer:",b)

    #long inetegers, There is no data type called long integer in python3
    longInt=4567812391234
    print ("Long integer and has no limit:",longInt)

    #Boolean
    error=False
    print ("Boolean:",error)

    #Strings
    str="john doe"
    char="c"
    print ("Strings:",str)
    print ("Characters:",char)

    #Collections
    #Dictionary or HashMap or HashTable
    myDictionary={
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print("Collection: Dictionary",myDictionary)

    #Set : Sets are unordered, so the items will appear in a random order.
    setOfFruits = {"apple", "banana", "cherry"}
    print("Collection: Set",setOfFruits)


# call functions
primitiveTypes()
