from selenium.webdriver.common.by import By
from Day1.Locator.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_xpath = Locators.welcome_link_xpath
        self.logout_xpath = Locators.logout_xpath

    def click_welcome(self):
        self.driver.find_element(By.XPATH, self.welcome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()