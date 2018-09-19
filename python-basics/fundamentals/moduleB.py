
# ---------------------------------------------------------
# moduleB.py
# A second user-defined module which defines a function and
# imports the other user-defined module as well as a 
# standard module.

from moduleA import funcA

def funcB( a ) :
  b = funcA( a, a * 4 )
  return b / 3 + funcC()

def funcC( x = 0 ) :
  return x * 12