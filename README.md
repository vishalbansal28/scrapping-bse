# BSE Data Scraper

This Python script allows you to scrape corporate announcement data from the Bombay Stock Exchange (BSE) website and store it in both an Excel file and a MongoDB database.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/bse-data-scraper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd bse-data-scraper
    ```

3. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
# For get_bse_data.py:
1. Run the `scrape_data.py` script:

    ```bash
    python scrape_data.py
    ```

2. Follow the prompts to enter the security name, from date, to date, and category for scraping.

3. The script will scrape the data, save it to an Excel file named `extracted_data.xlsx`
  
  
# For store_data_mongodb.py
# Excel to MongoDB Converter

This Python script (`store_data_mongodb.py`) allows you to convert data from an Excel file into MongoDB and upload it to a database collection.

## Usage

1. Ensure you have a MongoDB database set up and running.

2. Run the `store_data_mongodb.py` script:

    ```bash
    python store_data_mongodb.py
    ```

3. The script will read data from the Excel file `extracted_data.xlsx`, convert it into MongoDB documents, and upload it to the specified database collection.

## Configuration

You may need to configure the MongoDB connection string in the `scrape_data.py` script to match your MongoDB setup. Update the following line with your MongoDB connection string:

```python
client = MongoClient('mongodb+srv://username:password@cluster.mongodb.net/')
```

### Replace username, password, and cluster.mongodb.net with your MongoDB credentials and cluster details.

## Requirements
Python,
Selenium,
Pandas,
Openpyxl,
PyMongo.

## About the Script
# Purpose
This script is designed to automate the process of scraping corporate announcement data from the BSE website. It fetches information such as heading, PDF link, and XBRL code from the announcement tables.

## How it Works
The script launches a Chrome WebDriver and navigates to the BSE corporate announcements page.
It prompts the user to input the security name, from date, to date, and category for scraping.
Using Selenium, it interacts with the webpage to input the provided information and submit the form.
The script then scrapes data from the announcement tables, including headings, PDF links, and XBRL codes.
It saves the extracted data to an Excel file named extracted_data.xlsx.
Additionally, it uploads the data to a MongoDB database for storage.


## Technologies Used
Python: The script is written in Python, making use of various libraries such as Selenium, Pandas, and PyMongo.
Selenium: Used for web scraping and browser automation.
Pandas: Utilized for data manipulation and conversion.
Openpyxl: Used to interact with Excel files.
PyMongo: Used to interact with MongoDB databases.
