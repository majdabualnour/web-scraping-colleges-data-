from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
def gitdataf( ff ):
    def gitdata(driver, f):
        # Visit the webpage
        driver.get(f"{f}/admissions")

        # Wait for the element to be visible
        wait = WebDriverWait(driver, 20)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-testid='acceptance-rate-value']")))
        element1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-testid='sat-total-range-value']")))
        element2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-testid='regular-decision-value']")))
        element3 = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-testid='3.75+-value']")))
        element4 = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-testid='high-school-gpa-value']")))
        element5 = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-testid='high-school-rank-value']")))
        element6 = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-testid='college-prep-courses-value']")))
        element7 = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-testid='sat/act-scores-value']")))
        element8 = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-testid='recommendations-value']")))
        element9 = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-testid='apply-link-id']")))
        
        href = element9.get_attribute("href")
        data = element.text
        data2 = element1.text
        data3 = element2.text
        data4 = element3.text
        data5 = element4.text
        data6 = element5.text
        data7 = element6.text
        data8 = element7.text
        data9 = element8.text
        return data , data2 , f'3.75+:{data4}' , data3 , f'High School GPA : {data5} \nHigh School Rank : {data6}\nCollege Prep Courses : {data7}\nSAT/ACT Scores : {data8}\nRecommendations : {data9}',href  

        # Close the webdriver
        driver.quit()

    # Set up the Selenium webdriver with the Firefox driver
    options = Options()
    options.headless = True  # Run Firefox in headless mode (without opening a visible browser window)
    options.set_preference("dom.webnotifications.enabled", False)

    # Set up the Selenium webdriver with the Firefox driver and specified options
    driver = webdriver.Firefox(options=options)

    driver.get("https://bigfuture.collegeboard.org/colleges")



    # Set up the Selenium webdriver with the Firefox driver
    wait = WebDriverWait(driver, 20)

    search_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'cs-college-search-header-button') and contains(@class, 'cb-btn') and contains(@class, 'cs-secondary-btn')]")))
    # Find the search button element and perform a click action
    # search_button = wait.until(EC.visibility_of_element_located((By.XPATH, ""))
    search_button.click()
    driver.implicitly_wait(10)
    # Find the search bar element and enter the specific text
    search_bar = driver.find_element(By.ID, "cs-college-list-search-college-name-th-input")
    search_text = f"{ff}"
    search_bar.send_keys(search_text)
    search_bar.send_keys(Keys.RETURN)

    # Wait for the page to load and find the first result
    driver.implicitly_wait(10)

    first_result = driver.find_element(By.XPATH, "//li[contains(@class, 'typeahead-item-container')]")

    # Click on the first result
    first_result.click()

    # Call gitdata() function to extract data
    return gitdata(driver, driver.current_url)
