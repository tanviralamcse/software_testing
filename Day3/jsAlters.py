import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com")

# Alert Box starts here
# driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button[1]").click()
# time.sleep(3)
# alert = driver.switch_to.alert
# alert.accept()

# # Pop up box starts here
# driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button[2]").click()
# time.sleep(3)
# alert = driver.switch_to.alert
# alert.accept()
# # alert.dismiss() #to cancel
# time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button[3]").click()
prompt_dialog = driver.switch_to.alert
prompt_dialog.send_keys("Tanvir Alam")
prompt_dialog.accept()
time.sleep(3)

driver.quit()