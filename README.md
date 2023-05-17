# webCrawler
## async 104 job
``` py
async def main():
  links = []
  for page in range(1, 20):
    url =f'https://www.104.com.tw/jobs/search/?ro=0&isnew=30&kwop=7&keyword=Python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001008000&order=15&asc=0&page={page}&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1'
    links.append(url)

  async with ClientSession() as session:
    tasks = [asyncio.create_task(fetch(link, session)) for link in links]
    await asyncio.gather(*tasks)

async def fetch(link, session):
  async with session.get(link) as response:
    html = await response.text()
    soup = BeautifulSoup(html, 'lxml')
    blocks = soup.find_all('div', {'class': "b-block__left"})

    for block in blocks:
      job = block.find('a', {'class': "js-job-link"})
      if job is None:
        continue

      company = block.find_all('li')[1] 
      salary_ = block.find('a', {'class': "b-tag--default"})
      salary = block.find('span', {'class': "b-tag--default"})

      print((job.text, ) + (company.getText().strip(),))
      if salary is None:
        print(salary_.text)
      else:
        print(salary.text)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

```
![image](https://github.com/RandomErwin/webCrawler/blob/main/非同步%20104%20job.png)

## content regular expression
``` py
with open('content.txt', 'w') as file:
    file.write(content)

import re
pattern = r'([A-Za-z]+)\.'
with open('content.txt', 'r') as file:
    content = file.read()

matches = re.findall(pattern, content)
result = []
for match in matches:
    result.append(match)
    
``` 
![image](https://github.com/RandomErwin/webCrawler/blob/main/正則表達式.png)

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
![image](https://github.com/RandomErwin/webCrawler/blob/main/資料庫connect.png)

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
![image](https://github.com/RandomErwin/webCrawler/blob/main/原始圖表.png) 
![image](https://github.com/RandomErwin/webCrawler/blob/main/更新圖表.png)
