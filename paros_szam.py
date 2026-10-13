import unittest

def sajat_positive(szam: int, szam2: int):
    if szam % 2 == 0 and szam2 % 2 == 0:
        return szam, szam2

class TestAddFunction(unittest.TestCase):
    def test_positive(self):
        ertek = sajat_positive(4, 100)
        self.assertTrue(ertek)

unittest.main()