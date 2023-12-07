import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Software_testing")
links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links: ", len(links))

link1 = driver.find_element(By.LINK_TEXT,"Concurrent testing")
link1_url = link1.get_attribute("href")
driver.execute_script("window.open('{}', '_blank');".format(link1_url))
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.quit()
