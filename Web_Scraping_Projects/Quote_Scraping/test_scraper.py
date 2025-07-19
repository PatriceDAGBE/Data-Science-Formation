import requests
from bs4 import BeautifulSoup

try:
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    print(soup.prettify())
except ImportError:
    print("html5lib is not installed. Please run 'pip install html5lib' to install it.")
except Exception as e:
    print(f"An error occurred: {e}")