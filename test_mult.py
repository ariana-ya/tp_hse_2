import unittest
from functions import _mult

class Min(unittest.TestCase):
    def test_mult(self):
        self.assertEqual(_mult([1, 2, 3, 4, 5, 6, 7, 8, 9]), 362880)

    def test_mult1(self):
        self.assertEqual(_mult([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 0)

    def test_mult2(self):
        self.assertEqual(_mult([123, 456, 789]), 44253432)

    def test_mult3(self):
        self.assertEqual(_mult([1**2, 3**4, 4**5, 6**7, 8**9]), 3116402981210161152)

    def test_mult4(self):
        self.assertEqual(_mult([9, 9, 9, 9, 9]), 59049)