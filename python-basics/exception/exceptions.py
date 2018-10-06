
def catchingException():
    # In python exception can be handled by using try.. exception block
    try:
        myList = [12, 50, 5, 17]
        print(myList[4])
    except IndexError:
        print("Error: Index out of range.")

    # Multiple except block
    try:
        x = 0
        myList = [12, 50, 5, 17]
        print(myList[3] / x)
    except IndexError:
        print("Error: Index out of range.")
    except ZeroDivisionError:
        print("Error: Attempt to divide by zero.")
    except:
        print("Error: An exception was raised.")

def average( valueList ) :
   total = 0
   for x in valueList :
      total = total + x

   try:
      avg = total / len( valueList )
      return avg

   except ZeroDivisionError:
      return 0.0
      
catchingException()
