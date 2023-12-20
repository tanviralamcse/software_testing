from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException

# Set up the webdriver
driver = webdriver.Chrome()  # Use the appropriate webdriver for your browser

# Load the page with the elements containing href links
driver.get("https://www.healthline.com/search?q1=eczema")

# Wait for the page to load (you may need to adjust the wait time)
driver.implicitly_wait(10)

# Specify the target class for the elements with href links
target_class = 'css-nw354e'

# Function to collect href links from elements with a specified class
def collect_links():
    try:
        elements_with_links = driver.find_elements(By.CLASS_NAME, target_class)
        return [element.get_attribute("href") for element in elements_with_links]
    except StaleElementReferenceException:
        # If a StaleElementReferenceException occurs, refresh the page and try again
        print("Stale element reference. Refreshing the page.")
        driver.refresh()
        driver.implicitly_wait(10)
        return collect_links()

# Function to click on the next page based on the page number
def click_next_page(page_number):
    try:
        next_page_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//a[@aria-label="Page {page_number}"]'))
        )
        next_page_link.click()
        return True
    except (NoSuchElementException, TimeoutException):
        return False

# Collect and save links from all pages
current_page = 1
pages_clicked = 0  # Counter variable
while True:
    # Collect and save links from the current page
    href_links = collect_links()
    with open("output.txt", "a") as file:
        for link in href_links:
            file.write(link + "\n")

    # Increment the page number and click on the next page
    current_page += 1
    if not click_next_page(current_page):
        # Break the loop if there is no more next page
        print(f"No more pages. Clicked {pages_clicked} pages.")
        break

    # Increment the counter for each successfully clicked page
    pages_clicked += 1

# Print the total number of pages clicked
print(f"Total pages clicked: {pages_clicked}")

# Close the webdriver
driver.quit()
