import unittest
from calculate import canIBuyBeer

class TestBeer(unittest.TestCase):
    def test_when_17_and_on_krogen_should_not_be_allowed(self):
        age = 17
        loc = "krogen"
        c = canIBuyBeer(age, loc)
        self.assertFalse(c)

    def test_when_18_and_on_krogen_should_be_allowed(self):
        age = 18
        loc = "krogen"
        c = canIBuyBeer(age, loc)
        self.assertTrue(c)

    def test_when_20_and_on_systemet_should_be_allowed(self):
        age = 20
        loc = "systemet"
        c = canIBuyBeer(age, loc)
        self.assertTrue(c)

    def test_when_19_and_on_systemet_should_not_be_allowed(self):
        age = 19
        loc = "systemet"
        c = canIBuyBeer(age, loc)
        self.assertFalse(c)

    def test_always_fails(self):
        self.assertTrue(False, "This test is designed to fail")

if __name__ == '__main__':
    unittest.main()