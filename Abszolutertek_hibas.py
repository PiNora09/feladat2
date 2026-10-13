import unittest

def sajat_abs(szam: int):
    if szam < 0:
        return -szam
    else:
        return szam

class TestAddFunction(unittest.TestCase):

    def test_one_negative(self):
        ertek = sajat_abs(-5)
        self.assertGreater(ertek, 0)

    def test_one_positive(self):
        ertek = sajat_abs(5)
        self.assertGreater(ertek, 0)

    def test_zero(self):
        ertek = sajat_abs(0)
        self.assertEqual(ertek, 0)

unittest.main()