import sqlite3
import datetime


def adapt_date(date_obj):
    return date_obj.strftime('%Y-%m-%d')

def convert_date(s):
    return datetime.datetime.strptime(s.decode('utf-8'),'%Y-%m-%d').date()


sqlite3.register_adapter(datetime.date, adapt_date) # python -> saltype 로 변환 즉 db로 들어갈때
sqlite3.register_converter('DATE', adapt_date) # 리턴되는 문자열을 datetime.date 객체로 변활하는 패턴을 꺼낼때
# db에서 파이썬을 꺼낼때

conn = sqlite3.connect('example.db',detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test (date_column DATE)")

today = datetime.date.today()
cur.execute("INSERT INTO test (date_column) VALUES (?)", (today,))

conn.close()
