import requests
from bs4 import BeautifulSoup
import pymysql

class Stock:

  def __init__(self, *stock_nums):
    self.stock_nums = stock_nums

  def scrape(self):

    result = list()
    for stock_num in self.stock_nums:
      res = requests.get(f"https://tw.stock.yahoo.com/quote/{stock_num}")
      soup = BeautifulSoup(res.text, 'lxml')
      stock_name = soup.find('h1',{'class':"C($c-link-text) Fw(b) Fz(24px) Mend(8px)"}).getText()
      stock_date = soup.find('span',{'class':"C(#6e7780) Fz(14px) As(c)"}).getText()
      ul = soup.find('ul',{'class':"D(f) Fld(c) Flw(w) H(192px) Mx(-16px)"})
      items = ul.find_all('li',{'class':"price-detail-item H(32px) Mx(16px) D(f) Jc(sb) Ai(c) Bxz(bb) Px(0px) Py(4px) Bdbs(s) Bdbc($bd-primary-divider) Bdbw(1px)"})
      data = tuple(item.find_all('span')[1].getText() for item in items)
      result.append((stock_name, stock_date) + data)
    return result

  def save(self, stocks):
    db_settings = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "xxxxx",
        "db": "stock",
        "charset": "utf8"
    }

    try:
      conn = pymysql.connect(**db_settings)
      with conn.cursor() as cursor:
        sql = """INSERT INTO market(stock_name,
                                    stock_date,
                                    final_price,
                                    opening_price,
                                    highest_price,
                                    lowest_price,
                                    average_price,
                                    transaction_value,
                                    yesterday_price,
                                    quote_change,
                                    ups_and_downs,
                                    total_value,
                                    yesterday_value,
                                    amplitude)
                 VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        for stock in stocks:
          cursor.execute(sql, stock)
        conn.commit()

    except Exception as ex:
      print("Exception:", ex)

stock = Stock('2451', '2330', '2454')
stock.save(stock.scrape())