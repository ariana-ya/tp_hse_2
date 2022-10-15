import unittest
from functions import _sum

class Min(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]), 45)

    def test_sum1(self):
        self.assertEqual(_sum([2*4, 3*5, 8*9]), 95)

    def test_sum2(self):
        self.assertEqual(_sum([6, 6, 6]), 18)

    def test_sum3(self):
        self.assertEqual(_sum([-2, 2, 6, 9, -4, 55, -33, -7, 13, -6, 4, -37]), 0)

    def test_sum4(self):
        self.assertEqual(_sum([1+9, 2+8, 3+7]), 30)