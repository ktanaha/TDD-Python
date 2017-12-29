import unittest
import doller
import franc

class MoneyTest(unittest.TestCase):

    def test_doller_multiplication(self):
        five = doller.Doller(5)
        self.assertEqual(doller.Doller(10), five.times(2))
        self.assertEqual(doller.Doller(15), five.times(3))

    def test_Equality(self):
        self.assertTrue(doller.Doller(5) == doller.Doller(5))
        self.assertFalse(doller.Doller(5) == doller.Doller(6))
        self.assertTrue(franc.Franc(5) == franc.Franc(5))
        self.assertFalse(franc.Franc(5) == franc.Franc(6))
        self.assertFalse(doller.Doller(5) == franc.Franc(5))

    def test_franc_multiplication(self):
        five = franc.Franc(5)
        self.assertEqual(franc.Franc(10), five.times(2))
        self.assertEqual(franc.Franc(15), five.times(3))

if __name__ == '__main__':
    unittest.main()