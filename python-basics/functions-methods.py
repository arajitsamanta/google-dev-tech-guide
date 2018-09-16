
#Some functions are very common and are part of the Python language itself These built-in functions are considered to be 
#global to the program. Thus, they are always available and can be invoked using only the function name.
#When passing parameters to a function, the reference to the object is passed and not the value itself. This is the 
#expected behavior since Python represents all data as objects and all variables contain references

def builtinFunc():
    #Compute the absolute value of the integer x
    y = abs( -1.5 )
    print(y)

    #Create a complex number with real value r and imaginary i.
    z = complex( 5, 6 )
    print(z)
 
def userDefinedFuncWithReturnVal(x):
  return x**x

builtinFunc()
print(userDefinedFuncWithReturnVal(4))