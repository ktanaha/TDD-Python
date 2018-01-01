import unittest as ut
from money.money import Money

class MoneyTest(ut.TestCase):

    def test_multiplication(self):
        five = Money.doller(5)
        self.assertEqual(Money.doller(10), five.times(2))
        self.assertEqual(Money.doller(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.doller(5) == Money.doller(5))
        self.assertFalse(Money.doller(5) == Money.doller(6))
        self.assertFalse(Money.doller(5) == Money.franc(5))

    def test_currency(self):
        self.assertEqual('USD', Money.doller(2).currency())
        self.assertEqual('CHF', Money.franc(3).currency())

if __name__ == '__main__':
    ut.main()