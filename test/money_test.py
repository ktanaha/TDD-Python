import unittest as ut
from money.doller import Doller
from money.franc  import Franc

class MoneyTest(ut.TestCase):

    def test_doller_multiplication(self):
        five = Doller(5)
        self.assertEqual(Doller(10), five.times(2))
        self.assertEqual(Doller(15), five.times(3))

    def test_Equality(self):
        self.assertTrue(Doller(5) == Doller(5))
        self.assertFalse(Doller(5) == Doller(6))
        self.assertTrue(Franc(5) == Franc(5))
        self.assertFalse(Franc(5) == Franc(6))
        self.assertFalse(Doller(5) == Franc(5))

    def test_franc_multiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))

if __name__ == '__main__':
    ut.main()