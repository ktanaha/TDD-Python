import unittest
import doller

class MoneyTest(unittest.TestCase):

    def test_multiplication(self):
        five = doller.Doller(5)
        product = five.times(2)
        self.assertEqual(10, product.get_amount())
        product = five.times(3)
        self.assertEqual(15, product.get_amount())

    def test_Equality(self):
        self.assertTrue(doller.Doller(5).equals(doller.Doller(5)))


if __name__ == '__main__':
    unittest.main()