import unittest
from point import Point


class TestPointClass(unittest.TestCase):

    def test_default_constructor(self):
        p = Point()
        self.assertEqual(p.getX(), 0)
        self.assertEqual(p.getY(), 0)

    def test_custom_constructor(self):
        p = Point(10, 20)
        self.assertEqual(p.getX(), 10)
        self.assertEqual(p.getY(), 20)

    def test_split(self):
        p = Point(10, 20)
        p.shift(10, 50)
        self.assertEqual(p.getX(), 20)
        self.assertEqual(p.getY(), 70)

    def test_string_represntation(self):
        p = Point(1,2)
        self.assertEqual(str(p),"(1, 2)")
    

if __name__ == '__main__':
    unittest.main()
