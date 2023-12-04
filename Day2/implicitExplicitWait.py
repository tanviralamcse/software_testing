import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("https://www.expedia.com/")
# Timeouts: Implicit wait sets a default timeout for the entire test runtime, while explicit wait sets timeouts for specific conditions.
# Condition: Implicit wait waits for an element to appear on the page, while explicit wait waits for a specific condition, such as the presence of an element or the element to be clickable.
# Scope: Implicit wait applies globally, while explicit wait applies locally to a specific element.
# Exception: Implicit wait throws a NoSuchElementException when the WebDriver cannot find the element within the specified timeout. In contrast, explicit wait throws a TimeoutException when the element doesn’t meet the condition within the specified timeout.
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//*[@id='multi-product-search-form-1']/div/div/div[1]/ul/li[2]/a").click()
driver.find_element(By.XPATH,"//*[@id='search_form_product_selector_flights']/div/div[1]/div/ul/li[2]/a").click()
driver.find_element(By.XPATH, "//*[@id='FlightSearchForm_ONE_WAY']/div/div[1]/div/div[1]/div/div/div[2]/div[1]/button").click()
time.sleep(7)
driver.find_element(By.ID, "origin_select").send_keys("Frankfurt")

# Wait for the list to be present on the page
wait = WebDriverWait(driver,10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'uitk-action-list')))

# Find the button corresponding to Frankfurt and click it
frankfurt_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Frankfurt (FRA - Frankfurt Intl.)')]")
frankfurt_button.click()

time.sleep(7)

driver.quit()