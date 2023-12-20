import unittest


class LoginTest(unittest.TestCase):
    def test_loginByTwitter(self):
        print("Twitter login")
        self.assertTrue(True)

    def test_loginByEmail(self):
        print("Email Login")
        self.assertTrue(True)

    def test_loginByFacebook(self):
        print("Facebook Login")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
