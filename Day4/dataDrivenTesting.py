import xlutils
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
path = "/Users/tanviralam/xlsx1.xlsx"
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

rows = xlutils.getRowCount(path,"Sheet1")
cols = xlutils.getColumnCount(path,"Sheet1")

print("Row Count = ",rows,"Columns Count = ",cols)

for r in range(2,rows+1):
    username = xlutils.readData(path,"Sheet1",r,1)
    password = xlutils.readData(path,"Sheet1",r,2)
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

    if driver.current_url == expected_url:
        print("Test Passed")
        xlutils.writeData(path,"Sheet1",r,3,"Test Passed")
        driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
    else:
        print("Test Failed")
        xlutils.writeData(path,"Sheet1",r,3,"Test Failed")

driver.quit()
