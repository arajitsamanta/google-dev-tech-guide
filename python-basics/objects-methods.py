#A class is used to define a class of objects and objects are created or instantiated from a class. 
#Once an object has been created, it can then be used. In Python, all literal values result in the 
#creation of objects.

import datetime

#creating objects and invoking methods
def createObjects():
    today=datetime.date(2018,9,12)
    print("Date:", today.weekday())

    #Invoke method directly
    today=datetime.datetime.now()
    print("Date with time:",today)

createObjects()