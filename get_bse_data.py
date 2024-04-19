from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def scrape_data(security_input, from_date, to_date):
    # Initialize Chrome webdriver
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.bseindia.com/corporates/ann.html")

        # Wait for 20 seconds after opening the website
        time.sleep(1)


        # Find the security input box
        security_input_box = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[1]/div[4]/div/form/div/input")

        # Input the security name
        security_input_box.clear()
        security_input_box.send_keys(security_input)

        # Click on the input box again to focus on it
        security_input_box.click()

        # Hit the Enter key
        security_input_box.send_keys(Keys.RETURN)

        # Click on the From Date input box to open the calendar picker
        from_date_input_box = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/input")
        from_date_input_box.click()

        # Select the From Date from the calendar picker
        select_date(driver, from_date)

        # Click on the To Date input box to open the calendar picker
        to_date_input_box = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[2]/div[4]/input")
        to_date_input_box.click()

        # Select the To Date from the calendar picker
        select_date(driver, to_date)


        # Find the dropdown menu element
        dropdown_menu = driver.find_element(By.ID, "ddlPeriod")

        # Create a Select object
        select = Select(dropdown_menu)

        # Select "Company Update" from the dropdown menu
        select.select_by_visible_text("Company Update")

         # Click on the submit button
        submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[3]/div[5]/input[1]")
        submit_button.click()

        # Wait for the page to load
        time.sleep(20)



    finally:
        # Close the webdriver session
        driver.quit()

def select_date(driver, date):
    # Click on the input field to trigger the calendar
    date_input_box = driver.find_element(By.XPATH, "//input[@type='text']")
    date_input_box.click()

    # Parse the date (assuming it's in DD/MM/YYYY format)
    day, month, year = map(int, date.split('/'))

    # Click on the corresponding day in the calendar
    date_element = driver.find_element(By.XPATH, f"//a[text()='{day}']")
    date_element.click()

# Default values
security_input = "RELIANCE INDUSTRIES LTD"
from_date = "01/01/2024"
to_date = "18/04/2024"

# Call the function to start scraping
scrape_data(security_input, from_date, to_date)
