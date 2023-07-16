from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options
import fff
import gfwsfsad
import re
import dfasdfsdf
import openpyxl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Load the Excel file
workbook = openpyxl.load_workbook('thefile.xlsx')

# Select the specific worksheet
worksheet = workbook['Sheet1']  # Replace 'Sheet1' with the name of your worksheet

# Specify the column letter
target_column = 'D'  # Replace with the desired column letter

# Retrieve data from the specific column
column_data = []

def getalluwnat(thenameofsomething):

    text = str(thenameofsomething)
    text =text.lower()
    text = text.strip()
    if 'university of' not in text:
        text = text.replace('university' , '' )
        # text= text.replace('college' , '')
    
        
    text = text.strip()
    # text = text.replace(' ','-')
    thenameofsomething = text
    def aihaga(g, driverd):
        driverd.get(f"https://www.google.com/search?q=toefl minimum requirements {g}")

        # Wait for 10 seconds for the page to load
        driverd.implicitly_wait(3)

        # Find and extract specific data using XPath

        element2 = driverd.find_element(By.XPATH, "//div[@class='IZ6rdc']")


        data2 = element2.text
        
        return data2
    def extract_numbers(text):
        numbers = re.findall(r'\d+', text)
        if [int(number) for number in numbers][0] > 30:
            return 'Safety Reach'
        elif 10<=[int(number) for number in numbers][0] <= 30:
            return 'Reach'
        else:
            return 'High Reach'
    # Set up the Selenium webdriver with the Firefox driver
    options = Options()
    options.headless = False  # Run Firefox in headless mode (without opening a visible browser window)
    options.set_preference("dom.webnotifications.enabled", False)

    # Set up the Selenium webdriver with the Firefox driver and specified options
    driver = webdriver.Firefox(options=options)

    driver.get("https://bigfuture.collegeboard.org/colleges")


    time.sleep(5)
    # Set up the Selenium webdriver with the Firefox driver

    # Find the search button element and perform a click action
    wait = WebDriverWait(driver, 20)

    search_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'cs-college-search-header-button') and contains(@class, 'cb-btn') and contains(@class, 'cs-secondary-btn')]")))
    search_button.click()
    driver.implicitly_wait(10)
    # Find the search bar element and enter the specific text
    search_bar = driver.find_element(By.ID, "cs-college-list-search-college-name-th-input")
    search_text = thenameofsomething
    search_bar.send_keys(search_text)
    search_bar.send_keys(Keys.RETURN)

    # Wait for the page to load and find the first result
    driver.implicitly_wait(10)

    first_result = driver.find_element(By.XPATH, "//li[contains(@class, 'typeahead-item-container')]")

    # Click on the first result
    first_result.click()
    # print("Landed Page URL:", driver.current_url)
    # Close the webdriver

    a ,b,c , d= fff.gitsta(driver,driver.current_url)
    z ,x,v,n,j ,o=gfwsfsad.gitdataf(thenameofsomething)


    # print(dfasdfsdf.anythiinks(f'what essay required to apply {thenameofsomething}'))
    driver.quit()
    return a ,b,c , d,z ,x,v,n,j ,o , extract_numbers(z) ,dfasdfsdf.anythiink(f'minumm toefle score {thenameofsomething}')
# print(getalluwnat('union university'))




for cell in worksheet[target_column]:
    if cell.value:
        column_data.append(cell.value)
nf  =0

# Print the retrieved data
for cell_value in column_data:
    nf +=1
    if nf >5:
        print(cell_value)
        o = getalluwnat(cell_value)
        
        print(o)
        valu1 , valu2,valu3,valu4,valu5,valu6,valu7,valu8,valu9,valu10,valu11,valu12 = o
        nfs = nf +1

        worksheet[f'B{nfs}'] = 'USA'
        worksheet[f'I{nfs}'] = 'Common Application'
        worksheet[f'C{nfs}'] = valu11
        worksheet[f'E{nfs}'] = valu5
        worksheet[f'H{nfs}'] = 'Not specified'
        worksheet[f'J{nfs}'] = valu2
        worksheet[f'K{nfs}'] = valu1
        worksheet[f'L{nfs}'] = valu3
        worksheet[f'M{nfs}'] = 'no data'
        worksheet[f'N{nfs}'] = valu4
        worksheet[f'O{nfs}'] = 'no data'
        worksheet[f'Q{nfs}'] = 'Not specified'
        worksheet[f'R{nfs}'] = valu8
        worksheet[f'S{nfs}'] = valu9
        worksheet[f'T{nfs}'] = valu12
        worksheet[f'U{nfs}'] = valu6
        worksheet[f'V{nfs}'] = valu7
        worksheet[f'W{nfs}'] = valu10
        worksheet[f'X{nfs}'] = 'N/A'
        worksheet[f'Y{nfs}'] = 'N/A'
        worksheet[f'Z{nfs}'] = 'YES'
        workbook.save('data.xlsx')
        
