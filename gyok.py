import unittest
import math

def sajat_gyok(szam: int):
    if szam < 0:
        return -szam
    else:
        return szam

class TestAddFunction(unittest.TestCase):

    def test_gyok(self):
        ertek = sajat_gyok(math.sqrt(2))
        self.assertTrue(ertek)

unittest.main()