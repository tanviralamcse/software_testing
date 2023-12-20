import unittest
from Day8.package1.TC_login import LoginTest
from Day8.package1.TC_signup import SignupTest
from Day8.package2.TC_payment import PaymentTest
from Day8.package2.TC_paymentReturn import PaymentReturn

test_case1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
test_case2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
test_case3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
test_case4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)


# creating test suits
sanityTestSuit = unittest.TestSuite([test_case1,test_case2])
functionalTestSuit = unittest.TestSuite([test_case3,test_case4])
masterTestSuit = unittest.TestSuite([test_case1,test_case2,test_case3,test_case4])
unittest.TextTestRunner(verbosity=2).run(masterTestSuit)