import unittest

from distributeCandies import DistributeCandies

class TestDistributeCandies(unittest.TestCase):

    def test_input1(self):
        candies=[1,1,2,2,3,3]
        dc = DistributeCandies()
        self.assertEqual(dc.perfomrDistribution(candies),3)
    
    def test_input2(self):
        candies=[1,1,2,3]
        dc = DistributeCandies()
        self.assertEqual(dc.perfomrDistribution(candies),2)


if __name__ == '__main__':
    unittest.main()
