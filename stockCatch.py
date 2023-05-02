import requests
from bs4 import BeautifulSoup

class Stock:
    def __init__ (self, *stock_nums):
        self.stock_nums = stock_nums

    def scrape(self):
        result =list()
        for stock_num in self.stock_nums:
            res = requests.get(f"https://tw.stock.yahoo.com/quote/{stock_num}")
            soup = BeautifulSoup(res.text, 'lxml')
            stock_name = soup.find('h1', {'class': "C($c-link-text) Fw(b) Fz(24px) Mend(8px)"}).getText()
            time = soup.find('span', {'class': "C(#6e7780) Fz(14px) As(c)"}).getText()
            market_date = time[5:15]
            market_time = time[16:]
            ul =soup.find('ul', {'class': "D(f) Fld(c) Flw(w) H(192px) Mx(-16px)"})
            items = ul.find_all('li', {'class': "price-detail-item H(32px) Mx(16px) D(f) Jc(sb) Ai(c) Bxz(bb) Px(0px) Py(4px) Bdbs(s) Bdbc($bd-primary-divider) Bdbw(1px)"})
            data = tuple(item.find_all('span')[1].getText() for item in items)
            result.append((stock_name, market_date, market_time) + data)
        return result

stock = Stock('2451', '2330', '2454')
print(stock.scrape())
