import unittest as ut
from money.money import Money
from money.bank import Bank
from money.sum import Sum

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

    def test_simple_addition(self):
        five = Money.doller(5)
        sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum, 'USD')
        self.assertEquals(Money.doller(10), reduced)

    def test_plus_return_sums(self):
        five = Money.doller(5)
        result = five.plus(five)
        sum = result
        self.assertEquals(five, sum.augend())
        self.assertEquals(five, sum.addend())

    def test_reduce_sum(self):
        sum = Sum(Money.doller(3), Money.doller(4))
        bank = Bank()
        result = bank.reduce(sum, 'USD')
        self.assertEquals(Money.doller(7), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.doller(1), 'USD')
        self.assertEquals(Money.doller(1), result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(Money.franc(2), 'USD')
        self.assertEquals(Money.doller(1), result)

if __name__ == '__main__':
    ut.main()