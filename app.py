
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
url = "https://bigfuture.collegeboard.org/colleges/bucknell-university/tuition-and-costs"



try:
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        html_content = response.text
        print(html_content)
    else:
        print("Failed to retrieve HTML content. Status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error occurred during the request:", str(e))
