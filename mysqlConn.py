import pymysql

db_settings = {'host': '127.0.0.1',
               'port': 3306,
               'user': 'root',
               'password': 'xxxxx',
               'db': 'stock',
               'charset': 'utf8'
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
                    VALUE('APPL', '2023.05.01', '502', '498.5', '502', '498.0', '501', '124.18', '493.5', '1.72%', '9', '24,803', '29,518', '0.81%')"""
        cursor.execute(sql)
    conn.commit()
    print("ok")

except Exception as ex:
    print(ex)