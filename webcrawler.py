import requests
res = requests.get('https://www.judicial.gov.tw/tw/np-118-1.html')
print(res.text)

from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text,"lxml")
type(soup)
print(soup.prettify())