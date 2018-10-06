import unittest
from point import Point
from line import Line

class TestLineClass(unittest.TestCase):

    def test_is_horizontal_line(self):
        p1 = Point(5, 6)
        p2 = Point(5, 6)
        line=Line(p1,p2)
        self.assertTrue(line.isHorizontal)
 
if __name__ == '__main__':
    unittest.main()
