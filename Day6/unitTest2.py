import unittest
from selenium import webdriver


class SearchEngines(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://google.com")
        print("Title of the pages is: " + self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://bing.com")
        print("Title of the pages is: " + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
