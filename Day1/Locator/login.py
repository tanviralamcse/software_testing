import unittest
from selenium import webdriver
from Day1.Pages.homePage import HomePage
from Day1.Pages.loginPage import LoginPage

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.submit_button_click()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
