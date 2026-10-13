import unittest

def gyak_jegy(szam: int):
    return szam

class TestAddFunction(unittest.TestCase):
    def test_ot(self):
        ertek = gyak_jegy(90)
        self.assertEqual(ertek, )

    def test_negy(self):
        ertek = gyak_jegy(72)
        self.assertEqual(ertek, )

    def test_harom(self):
        ertek = gyak_jegy(58)
        self.assertEqual(ertek, )

    def test_ketto(self):
        ertek = gyak_jegy(53)
        self.assertEqual(ertek, )

    def test_egy(self):
        ertek = gyak_jegy(10)
        self.assertEqual(ertek, )

    def test_szoveg(self):
        ertek = gyak_jegy()

unittest.main()