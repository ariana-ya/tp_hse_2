import unittest
from functions import _sum, _mult

class MinMax(unittest.TestCase):
    def test_like(self):
        self.assertGreater(_mult([1, 2, 3, 4, 5]), _sum([1, 2, 3, 4, 5]))