# -*- coding: utf-8 -*-
"""Goodinfo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14f53I5vA1Pe1jtpZ-L1NtlJh9uf_d4oF
"""

import urllib.request as req
url = ' https://goodinfo.tw/tw/StockBzPerformance.asp?STOCK_ID=2330'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
request = req.Request(url, headers = headers)

with req.urlopen(request) as response:
  data_ = response.read().decode("utf-8")

from bs4 import BeautifulSoup
soup = BeautifulSoup(data_, 'lxml')
data = soup.select_one("#txtFinDetailData")

import pandas as pd
dfs = pd.read_html(data.prettify())

len(dfs)

df = dfs[0]
df.columns = df.columns.get_level_values(0)
df.head()

