#bs4 test
#https://github.com/vprusso/youtube_tutorials/blob/master/web_scraping_and_automation/beautiful_soup/beautiful_soup_and_requests.py

import requests
from bs4 import BeautifulSoup

URL = 'https://store.steampowered.com/games/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')
links = soup.find_all("a")
#inks)
print('\n')
#title = soup.find(id="productTitle",)
#price = soup.find_all(id="priceblock_ourprice")
for link in links:
    if "VAMPIRE" in link.text.upper():
        print(link.attrs['href'])
#print(id)
