import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        # Use a context manager to ensure the WebDriver is closed properly
        with webdriver.Firefox() as driver:
            driver.get("https://www.google.com")
            webpageTitle = driver.title
            self.assertEqual("Google", webpageTitle, "webpage title is not same")
            driver.quit()
if __name__ == "__main__":
    unittest.main()
