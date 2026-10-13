import unittest

def sajat_szamologep(szam: float, szam2: float, muvelet: str):
    if szam and szam2 == "+":
        return szam + szam2
    elif szam and szam2 == "-":
        return szam - szam2
    elif szam and szam2 == "*":
        return szam * szam2
    elif szam and szam2 == "/":
        return szam / szam2
    
class TestAddFunction(unittest.TestCase):
    def test_szamologep(self):
        ertek = sajat_szamologep(3.8, 4.2, "*")
        self.assertTrue(ertek)

    def test_zero(self):
        ertek = sajat_szamologep(3.8, 0.0, "/")
        self.assertEqual(ertek, 0)

unittest.main()