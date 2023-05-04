# webCrawler

## Connection
``` py
db_setting = { "host": "127.0.0.1",
               "port": 3306,
               "username": "root",
               "password": "xxxxx",
               "charset": "utf8"
}

conn = pymysql.connect(*db_setting)
with conn.cursor() as cursor:
  
  cursor.commit()
``` 
