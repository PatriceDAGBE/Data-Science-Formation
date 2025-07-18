# import requests
# from bs4 import BeautifulSoup

# base_url = "http://quotes.toscrape.com/"

# url = "/page/1"

# while url:

#     response = requests.get(f"{base_url}{url}", timeout=5)
#     print(f"Now Scraping{base_url}{url}")
#     response.raise_for_status()

#     soup = BeautifulSoup(response.content, 'html5lib')

#     print(soup)

#This will not run on online IDE
import requests
from bs4 import BeautifulSoup

URL = 'http://www.values.com/inspirational-quotes&quot'
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())