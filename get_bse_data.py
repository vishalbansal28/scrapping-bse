from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import openpyxl
from selenium.webdriver.common.action_chains import ActionChains

def extract_xbrl_link(driver, xbrl_element):

    # Scroll to the XBRL element
    actions = ActionChains(driver)
    actions.move_to_element(xbrl_element).perform()

    # Click on the XBRL box to open the new page
    xbrl_element.click()

    # Wait for the new page to load
    try:
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    except TimeoutException:
        print("New window did not open within the timeout.")
        return None
    
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])



    # Get the URL of the new page
    xbrl_url = driver.current_url

    # Close the new window
    driver.close()

    # Switch back to the original window
    driver.switch_to.window(driver.window_handles[0])

    return xbrl_url


def extract_data_from_sub_tables(driver):
    # Find the main table element by XPath
    main_table = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[2]/div/div[3]/div/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[4]/td")
    
    # Find all sub-tables within the main table by XPath
    sub_tables = main_table.find_elements(By.XPATH, "./table")
    
    # Initialize lists to store extracted data
    all_data = []

    # Iterate over each sub-table
    for table in sub_tables:
        # Extract data from the current sub-table
        heading_element = table.find_element(By.XPATH, "./tbody/tr[1]/td[1]/span")
        heading = heading_element.text.strip() if heading_element else ""
        
        pdf_link = ""
        try:
            pdf_link_element = table.find_element(By.XPATH, "./tbody/tr[1]/td[4]/a")
            pdf_link = pdf_link_element.get_attribute("href")
        except NoSuchElementException:
            pass
        
        xbrl_element = table.find_element(By.XPATH, "./tbody/tr[1]/td[5]/a")
        xbrl_link = extract_xbrl_link(driver, xbrl_element)
        
        # Append the extracted data to the list
        all_data.append({
            'Heading': heading,
            'PDF Link': pdf_link,
            'XBRL Code': xbrl_link
        })
    
    return all_data



def scrape_data(security_input, from_date, to_date, category):
   
    # Initialize Chrome webdriver
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.bseindia.com/corporates/ann.html")

        # Find the security input box
        security_input_box = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[1]/div[4]/div/form/div/input")

        # Input the security name
        security_input_box.clear()
        security_input_box.send_keys(security_input)

        # Wait for the dropdown list to appear
        wait = WebDriverWait(driver, 10)
        # Wait for the dropdown list to be visible
        dropdown_list = wait.until(EC.visibility_of_element_located((By.ID, "ulSearchQuote2")))

        # Select the desired option from the dropdown list (assuming it's the first option)
        dropdown_list.click()

        # Hit the Enter key
        security_input_box.send_keys(Keys.RETURN)

        # Wait for some time for the page to load
        time.sleep(1)

        # Click on the From Date input box to open the calendar picker
        # Call the function for both from_date and to_date inputs
        select_date(driver, from_date, "/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/input", "/html/body/div[6]")
        select_date(driver, to_date, "/html/body/div[1]/div[5]/div[1]/div[2]/div[4]/input", "/html/body/div[6]")

        # Find the dropdown menu element
        dropdown_menu = driver.find_element(By.ID, "ddlPeriod")

        # Create a Select object
        select = Select(dropdown_menu)

        # Select "Company Update" from the dropdown menu
        select.select_by_visible_text(category)

         # Click on the submit button
        submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[3]/div[5]/input[1]")
        submit_button.click()

        # Wait for the page to load
        time.sleep(2)

        # Create a workbook to store all data
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.append(["Heading", "PDF Link", "XBRL Code"])

        while True:
            # Extract data from sub-tables
            data = extract_data_from_sub_tables(driver)

            # Append the data to the workbook
            for row in data:
                worksheet.append([row["Heading"], row["PDF Link"], row["XBRL Code"]])

            try:
                # Check if there is a next page button
                next_page_button = wait.until(EC.element_to_be_clickable((By.ID, "idnext")))

                # Scroll to the element
                driver.execute_script("arguments[0].scrollIntoView(true);", next_page_button)

                # Add a small delay after scrolling
                time.sleep(1)

                # Click the next page button
                next_page_button.click()
                time.sleep(2)  # Wait for the new page to load
            except TimeoutException:
                # If there is no next page button, break the loop
                break

        # Save the workbook to an Excel file
        excel_file_path = "extracted_data.xlsx"
        workbook.save(excel_file_path)
        print(f"Data saved to {excel_file_path}")

    finally:
        # Close the webdriver session
        driver.quit()


    
def select_date(driver, date, input_box_xpath, calendar_xpath):
    # Define month names
    calendar_month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
     # Click on the input field to trigger the calendar
    date_input_box = driver.find_element(By.XPATH, input_box_xpath)
    date_input_box.click()

    # Parse the date (assuming it's in DD/MM/YYYY format)
    day, month, year = map(int, date.split('/'))

    # Click on the year dropdown menu and select the year
    year_dropdown = driver.find_element(By.XPATH, f"{calendar_xpath}/div/div/select[2]")
    year_dropdown.click()
    year_option = year_dropdown.find_element(By.XPATH, f"option[@value='{year}']")
    year_option.click()

    # Click on the month dropdown menu and select the month
    month_dropdown = driver.find_element(By.XPATH, f"{calendar_xpath}/div/div/select[1]")
    month_dropdown.click()
    month_option = month_dropdown.find_element(By.XPATH, f"option[text()='{calendar_month_names[month - 1]}']")  # Assuming month names are stored in a list called calendar_month_names
    month_option.click()

    # Click on the corresponding day in the calendar
    date_element = driver.find_element(By.XPATH, f"{calendar_xpath}/table/tbody/tr/td/a[text()='{day}']")
    date_element.click()


   

# Default values
security_input = input("Enter the security name: ")
from_date = input("Enter the From date (DD/MM/YYYY): ")
to_date = input("Enter the To date (DD/MM/YYYY): ")
category = input("Enter the category: ")

# Call the function to start scraping
scrape_data(security_input, from_date, to_date, category)
