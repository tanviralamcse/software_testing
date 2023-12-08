import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")
print(driver.find_element(By.TAG_NAME,"body").text)
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")
print(driver.find_element(By.TAG_NAME,"body").text)
time.sleep(2)
driver.quit()

