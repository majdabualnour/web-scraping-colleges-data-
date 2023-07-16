from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
def gitsta(driver ,f):
# Create Firefox options and set profile preferences to disable notifications
    # options = Options()
    # options.headless = False  # Run Firefox in headless mode (without opening a visible browser window)
    # options.set_preference("dom.webnotifications.enabled", False)

    # # Set up the Selenium webdriver with the Firefox driver and specified options
    # driver = webdriver.Firefox(options=options)


    # Visit the webpage
    driver.get(f"{f}/tuition-and-costs")

    # Wait for 10 seconds for the page to load
    driver.implicitly_wait(3)
    wait = WebDriverWait(driver, 20)
    try:
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@id='csp-list-item-private-tuition-value']")))
        data = element.text
    except:
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@id='csp-list-item-in-state-tuition-value']")))
        elementex = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@id='csp-list-item-out-of-state-tuition-value']")))
        data = element.text
        dataex = elementex.text
        data = f'In-State Tuition : {data}\nOut-of-State Tuition : {dataex}'
    element2 = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@id='csp-list-item-average-housing-value']")))
    element3 = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@id='csp-list-item-books-and-supplies-value']")))
    element4 = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@id='csp-list-item-transportation-value']")))
    # Find and extract specific data using XPath

    
    data2 = element2.text
    data3 = element3.text
    data4 = element4.text
    return data2, data, data3, data4

    # Close the webdriver
   

def gitdata(driver, f):
    # Visit the webpage
    driver.get(f"{f}/admissions")

    # Wait for the element to be visible
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@data-testid='acceptance-rate-value']")))

    data = element.text
    print("Acceptance Rate:", data)

    # Close the webdriver
    driver.quit()

    # Close the webdriver
    driver.quit()
def gitname(text):
    text = str(text)
    text =text.lower()
    text = text.strip()
    if 'university of' not in text:
        text = text.replace('university' , '' )
    if 'college' not in text:
        text= text.replace('college' , '')
    text = text.strip()
    text = text.replace(' ','-')
    return text


    