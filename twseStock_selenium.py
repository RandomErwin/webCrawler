from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 
import time

options = Options()
options.chrome_executable_path = "/usr/local/bin/chromedriver"
browser = webdriver.Chrome(options = options)
browser.get("https://www.twse.com.tw/zh/trading/historical/stock-day-avg.html")

class StockPrice:
    def __init__ (self, *stockNums):
        self.stockNums =stockNums

    def info(self, year, month):
        selectYear = Select(browser.find_element("name", 'yy'))
        selectYear.select_by_value(year)
        selectMonth = Select(browser.find_element("name", 'mm'))
        selectMonth.select_by_value(month)

        stockNo = browser.find_element("name", 'stockNo')
        result = []
        for stockNum in self.stockNums:
            stockNo.clear()
            stockNo.send_keys(stockNum)
            stockNo.submit()

            time.sleep(3)

            soup = BeautifulSoup(browser.page_source, 'lxml')
            div = soup.find('div', {'class': "rwd-table dragscroll sortable F1 R2_"})
            bodys = div.find('tbody', {'class': "is-last-page"})
            daliy = tuple(body.find_all('td')[0].getText() for body in bodys)
            prices = tuple(body.find_all('td')[1].getText() for body in bodys)
            result.append(daliy + prices)
        
        print(result)
            

stock = StockPrice('2330', '2454')
stock.info("2023", "1")
