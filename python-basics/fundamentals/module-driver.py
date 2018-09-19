# module-driver.py
# The driver file which contains the statements creating
# the main flow of execution.

# ***** Importing Modules ******
#The modules are simply Python source files and thus have a .py extension. When importing a module, however, you omit the extension. 
#The examples in this book assume the modules are stored in the same directory as the driver program.

import moduleA
import moduleB

# ***** Multiple Exclusion *****
#Module moduleA is imported in both module-driver.py and moduleB.py since its contents is used in both. The Python interpreter will only import
#a module once, even if it encountered multiple times. You should import a module within a source file if any component of that module
#is used. Let the interpreter omit it, if it has already been included.

value1 = int( input( "Enter value one: " ) )
value2 = int( input( "Enter value two: " ) )
resultA = moduleA.funcA( value1, value2 )
resultB = moduleB.funcB( resultA )
print("Results = ", resultA, resultB)

# ***** Multiple Exclusion *****
"""
ll identifiers in Python live within a namespace — the context in which identifers are defined. You can think of a namespace as a container or index in which various identifiers are stored. When an indentifer is referenced in a Python program, a search is performed in particular namespace to determine if that identifier is valid. The namespace concept allows us to create duplicate names, each existing in a different namespace.

In Python, each module constitutes its own namespace. Any identifier declared within a module, may be freely used within that same module. Consider the moduleB module from above which defines two functions, funcB() and funcC(). Notice that funcC() is called from within funcB()

def funcB( a ) :
  b = funcA( a, a * 4 )
  return b / 3 + funcC()
 
which is valid since both are in the same namespace. But what about the call to funcA()? There is no such function within the moduleB module. That function resides in the module moduleA and was made available via the statement

from moduleA import *
 
When the from/import statement is used, it includes the module and makes its contents available for use in the current module, but it also includes the identifiers from the imported module into the namespace of the current module. That is why we can refer to funcA() as if it were defined within the moduleB namespace, even though it was defined within the moduleA namespace. The same is true for the sqrt() function used in the module moduleA. That function was defined in the math namespace, but has been imported and made a part of the moduleA namespace.
"""