import unittest


class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("this is a login test")
    @classmethod
    def tearDown(self):
        print("This is a logout test")

    @classmethod
    def setUpClass(cls):
        print("Application is opening..... ")

    @classmethod
    def tearDownClass(cls):
        print(".....logging out from app;ication ")
    def test_search(self):
        print("Search test  ")

    def test_advancedsearch(self):
        print("Search Advanced test  ")

    def test_prepaidRecharge(self):
        print("Search Prepaid Recharge  ")

    def test_postPaid(self):
        print("Search PostPaid Recharge  ")


if __name__ == '__main__':
    unittest.main()
