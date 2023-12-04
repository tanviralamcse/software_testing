# Selenium Conditiaonal Commands is_Displayed, is_selected, is_enabled
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(3)
checkbox1 = driver.find_element(By.XPATH, "//*[@id='checkboxes']/input[1]")
print(checkbox1.is_enabled())  # return True or false
time.sleep(4)
checkbox2 = driver. find_element(By.XPATH, "//*[@id='checkboxes']/input[2]")
print(checkbox2.is_displayed())  # return True or False
time.sleep(3)
checkbox1 = driver.find_element(By.XPATH, "//*[@id='checkboxes']/input[1]")
print(checkbox1.is_selected())  # return false
time.sleep(4)
checkbox2 = driver. find_element(By.XPATH, "//*[@id='checkboxes']/input[2]")
print(checkbox2.is_selected())  # return True
driver.quit()
