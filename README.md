# webCrawler

## buy iphone
``` py
import pandas as pd
dfs = pd.read_html('https://www.cht.com.tw/home/apple/iphone/index')
df = dfs[0]

# 填滿填滿 month內的數字
df['month'] = df['month'].ffill()
# 移除資料為 na的列
df.dropna(inplace=True)
# 在df[]過濾包含“個月”的raw
df2 = df[~df['月繳金額.1'].str.contains('個月')]
df3 = pd.wide_to_long(df2, ['$'], i=['購機優惠價', '機型', '容量','month'], j='m_price', suffix='[\d,]+')
df3.reset_index(inplace=True)

#將 moth欄的資料轉換為 int型態
df4['month'] = df4['month'].astype(int)
# 將 m_price內的資料轉為 int型態
df4['m_price'] = df4['m_price'].map(lambda e: int(e.replace(',','')))
# 將 m_price內的資料轉為 int型態
df4['$'] = df4['$'].astype(int)

# 總價計算
df4['total'] = df4['month'] * df4['m_price'] + df4['$']
# 總價/綁訂月數
df4['avg'] = (df4['total'] / df4['month']).astype(int)
# 在綁定期間每月平均需付的金額
df4.sort_values('avg')

``` 

## content regular expression
``` py
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
    
``` 

## connection mysql
``` py
db_settings = {"host": "127.0.0.1",
               "port": 3306,
               "user": "root",
               "password": "yor passwword",
               "db": "your database name"
               "charset": "utf8"
}

try:
  conn = pymysql.connect(**db_settings)
  with conn.cursor() as cursor:
    sql = """INSERT INTO market(stock_name, market_time, price) 
             VALUE('TSMC', '2023.05.01', '502')"""
    cursor.execute(sql)
  conn.commit()
  
except Exception as ex:
  print(ex)
``` 
