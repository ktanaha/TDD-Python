import unittest as ut
from money.money import Money

class MoneyTest(ut.TestCase):

    def test_doller_multiplication(self):
        five = Money.doller(5)
        self.assertEqual(Money.doller(10), five.times(2))
        self.assertEqual(Money.doller(15), five.times(3))

    def test_Equality(self):
        self.assertTrue(Money.doller(5) == Money.doller(5))
        self.assertFalse(Money.doller(5) == Money.doller(6))
        self.assertTrue(Money.franc(5) == Money.franc(5))
        self.assertFalse(Money.franc(5) == Money.franc(6))
        self.assertFalse(Money.doller(5) == Money.franc(5))

    def test_franc_multiplication(self):
        five = Money.franc(5)
        self.assertEqual(Money.franc(10), five.times(2))
        self.assertEqual(Money.franc(15), five.times(3))

    def test_currency(self):
        self.assertEqual('USD', Money.doller(2).currency())
        self.assertEqual('CHF', Money.franc(3).currency())

if __name__ == '__main__':
    ut.main()