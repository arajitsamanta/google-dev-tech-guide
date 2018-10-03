# point.py
# Defines a class to represent two-dimensional discrete points.

class Point :

    #Python default constructor
   def __init__( self, x = 0, y = 0 ) :
      self.XCoord = x
      self.YCoord = y

   def __str__( self ) :
      return "(" + str( self.XCoord ) + ", " +  str( self.YCoord ) + ")"

   def getX( self ) :
      return self.XCoord

   def getY( self ) :
      return self.YCoord

   def shift( self, xInc, yInc ) :
      self.XCoord += xInc
      self.YCoord += yInc

p = Point()
print("Object instantiated with default values",p.getX(),p.getY())
p = Point(5,6)
print("Object instantiated with custom values",p.getX(),p.getY())
p.shift(10,50)
print("Updated object state",p.getX(),p.getY())
print("String representation of a python object",str(p))