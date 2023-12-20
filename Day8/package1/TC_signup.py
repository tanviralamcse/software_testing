import unittest


class SignupTest(unittest.TestCase):
    def test_signupByTwitter(self):
        print("signup Twitter login")
        self.assertTrue(True)

    def test_signupByEmail(self):
        print("signup Email Login")
        self.assertTrue(True)

    def test_signupByFacebook(self):
        print("signup Facebook Login")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
