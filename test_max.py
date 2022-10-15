import unittest
from functions import _max

class Max(unittest.TestCase):
    def test_max(self):
        self.assertEqual(_max([404, 505, 808]), 808)

    def test_max1(self):
        self.assertEqual(_max([-123456789, -12345, 0]), 0)

    def test_max2(self):
        self.assertEqual(_max([333/111, 333/3, 333/9]), 111)

    def test_max3(self):
        self.assertEqual(_max([9*9, 9**9, 9+9*9]), 387420489)

    def test_max4(self):
        self.assertEqual(_max([7, 7, 7, 7, 7]), 7)
