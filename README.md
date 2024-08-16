# University Requirements Data Extraction Script

This project automates the extraction of university application requirements, including TOEFL minimum scores and other relevant data, from web sources and updates an Excel file with the retrieved information.

## Overview

The script is designed to:

1. Read university names from an Excel file.
2. Use Selenium to search the web for specific university requirements.
3. Extract and categorize information such as TOEFL minimum scores, application types, and other data.
4. Write the extracted data back into the Excel file.

## Features

- **Web Scraping with Selenium:** Interacts with web pages to gather university application data.
- **Data Handling with OpenPyXL:** Reads from and writes to Excel files to manage the university data.
- **Automated Data Categorization:** Extracts numerical data and classifies it (e.g., "Safety Reach," "Reach," "High Reach").
- **Customizable Search:** The script can be adapted to search for different types of data based on your needs.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `selenium`
  - `openpyxl`
  - `re` (standard library)
  - Custom modules: `fff`, `gfwsfsad`, `dfasdfsdf` (Ensure these are installed or available in your project)

To install the necessary libraries, use:

```bash
pip install selenium openpyxl
```

## Setup

1. **Geckodriver:** Ensure that Geckodriver is installed and added to your system's PATH for Firefox WebDriver.

2. **Excel File:** Prepare an Excel file named `thefile.xlsx` with a worksheet named `Sheet1`. The university names should be listed in column `D`.

## Usage

1. **Run the Script:**

   ```bash
   python main.py
   ```



2. **Output:**
   - The script will update the Excel file with the extracted data, including information such as:
     - Column `B`: Country (e.g., "USA")
     - Column `C`: Minimum TOEFL score
     - Column `I`: Application type (e.g., "Common Application")
     - Other relevant columns based on the extracted data

## Code Breakdown

- **WebDriver Setup:** The script sets up a Firefox WebDriver in non-headless mode with notifications disabled.
- **Data Extraction:** The `getalluwnat` function handles the web scraping, data extraction, and categorization.
- **Excel File Handling:** The script reads from the Excel file, processes each university name, and updates the file with the retrieved data.

## License

This project is licensed under the MIT License.

## Acknowledgments

This project leverages several Python libraries and modules to automate data extraction and management.

