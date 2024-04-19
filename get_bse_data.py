from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_data(security_input, from_date, to_date):
    # Initialize Chrome webdriver
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.bseindia.com/corporates/ann.html")

        # Find the input fields and input the security name/code/id
        security_input_box = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[1]/div[4]/div/form/div/input")
        security_input_box.clear()
        security_input_box.send_keys(security_input)

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

        # Submit the form
        security_input_box.send_keys(Keys.RETURN)

        # Wait for the page to load
        WebDriverWait(driver, 20).until(EC.url_contains("some_identifier_in_the_url"))

        # Once the page has loaded, you can scrape the data from the page using BeautifulSoup or Selenium
        # For example:
        # soup = BeautifulSoup(driver.page_source, 'html.parser')
        # rows = soup.find_all('tr', class_='table-row')
        # (Scrape data as needed)

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
