import requests
from bs4 import BeautifulSoup

url = 'https://lawplayer.tw/blog/p/judgment-reading'
res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'lxml')
content = soup.getText()

with open('content.txt', 'w') as file:
    file.write(content)

import re
pattern = r'.{3}主文.{3}'
with open('content.txt', 'r') as file:
    content = file.read()

matches = re.findall(pattern, content)
result = []
for match in matches:
    result.append(match)

print(result)