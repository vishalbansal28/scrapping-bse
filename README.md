
## Scrapping-BSE

This repository contains a Python project for scraping corporate announcement data from the Bombay Stock Exchange (BSE) website. It includes data extraction, testing, MongoDB storage, and an automated Azure Pipeline for continuous integration.

**Project Structure**

```
scrapping-bse/
├── get_bse_data.py         # Main scraper script
├── store_data_mongodb.py   # Script for uploading scraped data to MongoDB
├── test_scrapper.py        # Unit tests for the scraper
├── requirements.txt       # List of Python dependencies
├── extracted_data.xlsx    # Sample Excel file (optional)
└── azure-pipelines.yml     # Azure Pipeline configuration
```

**Features**

* **Web Scraping:**  Uses Selenium to extract corporate announcements data from the BSE website, including headings, PDF links, and XBRL codes.
* **Data Storage:** Saves extracted data in an Excel file (`extracted_data.xlsx`) and uploads it to a MongoDB database.
* **Testing:**  Includes unit tests (using `pytest`) to verify the scraper's functionality.
* **Azure Pipeline:**  An automated pipeline (defined in `azure-pipelines.yml`) for:
    * Installing dependencies
    * Running tests
    * Uploading data to MongoDB
    * Publishing test results

**Prerequisites**

* Python 3.x
* MongoDB account (with a database and collection set up)
* ChromeDriver compatible with your environment (download from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads))
* Azure DevOps account (for running the pipeline)

**Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/scrapping-bse.git
   cd scrapping-bse
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

**Usage**

1. **Scrape Data:** Run `get_bse_data.py`. The script will prompt you for:
    * Security name
    * From date (YYYY-MM-DD)
    * To date (YYYY-MM-DD)
    * Category (e.g., Board Meetings, Financial Results)

2. **Upload to MongoDB:**  Run `store_data_mongodb.py` to upload data from `extracted_data.xlsx` to your MongoDB collection.

**Running the Azure Pipeline**

1. **Create a new pipeline:** Go to your Azure DevOps project and create a new pipeline.
2. **Choose YAML:** Select "YAML" as your pipeline type.
3. **Select Repository:** Choose your GitHub repository (`scrapping-bse`) and branch (`main`).
4. **Paste YAML:** Copy the content of `azure-pipelines.yml` into the editor.
5. **Customize:** Update the `artifactName` for ChromeDriver (if you're not using the automatic download).
6. **Save and Run:** Save the pipeline and run it.

**Troubleshooting**

* **ChromeDriver Compatibility:** Ensure you're using a ChromeDriver version compatible with your browser and operating system (OS).
* **MongoDB Connection:** Double-check your MongoDB connection string and authentication settings in `store_data_mongodb.py`.
* **Azure Pipeline Setup:** Ensure you've configured your pipeline properly, including the correct artifact name, script path, and any necessary secrets or variable groups.

**Contribute**

Feel free to contribute to this project by:

* **Submitting bug reports**
* **Suggesting improvements**
* **Adding new features**

**License**

This project is licensed under the MIT License.

**Disclaimer**

This project is for educational purposes only. It is provided "as is" without warranty of any kind. Use at your own risk. 

```
