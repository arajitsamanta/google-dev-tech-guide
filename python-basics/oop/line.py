#line.py
#Defines a geometric line in the two-dimensional Cartesian coordinate system; a Line line is composed of two Point objects.
from point import Point
import math


class Line :
   def __init__( self, fromPoint, toPoint ) :
      self.startPoint = fromPoint
      self.endPoint = toPoint

   def length( self ) :
      xDiff = self.startPoint.getX() - self.endPoint.getX()
      yDiff = self.startPoint.getY() - self.endPoint.getY()
      return math.sqrt( xDiff * xDiff + yDiff * yDiff )

   def slope( self ) :
      if self.isVertical() : 
         return None
      else :
         run = self.startPoint.getX() - self.endPoint.getX()
         rise = self.startPoint.getY() - self.endPoint.getY()
         return rise / float( run )

   def isVertical( self ) :
      return self.startPoint.getX() == self.endPoint.getX() 

   def isHorizontal( self ) :
      return self.startPoint.getY() == self.endPoint.getY() 

   def shift( self, x, y ) :
      self.startPoint.shift( x, y )
      self.endPoint.shift( x, y )

   def getStartPoint( self ) :
      return self.startPoint
      
   def getEndPoint( self ) :
      return self.endPoint


p1 = Point(5, 6)
p2 = Point(5, 6)
line=Line(p1,p2)
print(line.isHorizontal())