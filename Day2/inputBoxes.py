import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Tanvir")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("Alam")
driver.find_element(By.ID, "RESULT_TextField-3").send_keys("015739061235")
driver.find_element(By.ID, "RESULT_TextField-4").send_keys("Bangladesh")
driver.find_element(By.ID, "RESULT_TextField-5").send_keys("Dhaka")
driver.find_element(By.ID, "RESULT_TextField-6").send_keys("tanviralam.cse@gmail.com")
driver.find_element(By.XPATH, "//label[text()='Male']").click()

days_to_select = ["Sunday", "Wednesday", "Friday"]
for day in days_to_select:
    driver.find_element(By.XPATH, f"//label[text()='{day}']").click()
# driver.find_element(By.XPATH, "//label[text()='Sunday']").click()
# driver.find_element(By.XPATH, "//label[text()='Wednesday']").click()
# driver.find_element(By.XPATH, "//label[text()='Friday']").click()

list = Select(driver.find_element(By.ID, "RESULT_RadioButton-9"))
list.select_by_visible_text("Afternoon")  # Replace with the desired option text

file_input = driver.find_element("id", "RESULT_FileUpload-10")
file_path = "/Users/tanviralam/Downloads/thumb_nov22_03.jpg"
file_input.send_keys(file_path)

time.sleep(5)

driver.quit()
