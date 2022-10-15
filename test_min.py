import unittest
from functions import _min

class Min(unittest.TestCase):
    def test_min(self):
        self.assertEqual(_min([-1, 0, 1]), -1)

    def test_min1(self):
        self.assertEqual(_min([22, 33, 44, 0]), 0)

    def test_min2(self):
        self.assertEqual(_min([2*2, 3*4, 5*6]), 4)

    def test_min3(self):
        self.assertEqual(_min([-2, -3, -4]), -4)

    def test_min4(self):
        self.assertEqual(_min([0, 0, 0]), 0)

