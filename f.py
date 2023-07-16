import requests
from bs4 import BeautifulSoup

url = "https://bigfuture.collegeboard.org/colleges/bucknell-university/tuition-and-costs"
try:
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        html_content = response.text

        # Format the HTML code with each tag on a new line
        soup = BeautifulSoup(html_content, "html.parser")
        formatted_html = soup.prettify()

        print(formatted_html)
    else:
        print("Failed to retrieve HTML content. Status code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error occurred during the request:", str(e))
