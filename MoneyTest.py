import unittest
import doller

class MoneyTest(unittest.TestCase):

    def test_multiplication(self):
        five = doller.Doller(5)
        five.times(2)
        self.assertEqual(10, five.get_amount())

if __name__ == '__main__':
    unittest.main()