import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentinDollar(self):
        print("This is payment in $$$$ Dollar")
        self.assertTrue(True)

    def test_paymentinEuro(self):
        print("This is payment in ¢¢¢¢ Euro")
        self.assertTrue(True)

if __name__ == '__main__':
        unittest.main()
