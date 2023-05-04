# webCrawler

## Connection
``` py
db_settings = { "host": "127.0.0.1",
               "port": 3306,
               "username": "root",
               "password": "yor passwword",
               "db": "your database name"
               "charset": "utf8"
}
try:
  conn = pymysql.connect(*db_settings)
  with conn.cursor() as cursor:
    sql = """INSERT INTO market(stock_name, market_time, price) 
             VALUE('TSMC', '2023.05.01', '502')"""
    cursor.execute(sql)
  cursor.commit()
except Exception as ex:
  print(ex)
``` 
