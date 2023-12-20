import unittest

import random

number = random.randrange(1,10)
print(number)
class Apptesting(unittest.TestCase):

    def test_login(self):
        print("Login 1")

    @unittest.SkipTest
    def test_login2(self):
        print("Login 2")

    @unittest.skipIf(number%2!=0,"Odd Number")
    def test_login3(self):
        print("Login 3")

    @unittest.skipIf(number%2==0,"Even Number")
    def test_login4(self):
        print("Login 4")


if __name__ == '__main__':
    unittest.main()
