# pip install beautifulsoup4
# pip install required 
# pip install pandas

import requests 
from bs4 import BeautifulSoup

# streaming time period 04:08:33

page = requests.get()
soup = BeautifulSoup(page.content,'html.parser')