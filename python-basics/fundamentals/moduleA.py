# ---------------------------------------------------------
# moduleA.py
# A user-defined module which defines a function and
# imports a standard module.

from math import sqrt

def funcA( x, y ) :
  d = sqrt( x * x + y * y )
  return d