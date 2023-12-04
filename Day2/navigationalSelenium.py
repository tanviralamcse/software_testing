from selenium import webdriver
import time
# how to navigate from one page to another page
driver = webdriver.Firefox()
driver.get("https://www.google.com/search?q=sunset+frankfurt+fecenheim&oq=sunset+frankfurt+fecenheim&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAHSAQg5OTMyajFqN6gCALACAA&sourceid=chrome&ie=UTF-8")
driver.get("http://ww7.demoaut.com/?usid=20&utid=10680161746")
time.sleep(5)
driver.back()
time.sleep(4)
driver.forward()
time.sleep(3)
driver.quit()