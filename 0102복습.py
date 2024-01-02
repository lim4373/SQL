import sqlite3
# 1.연결 db생성
conn = sqlite3.connect("employee.db")
# 2. 커서 생성
cursor = conn.cursor()
#3. 테이블 생성    employees    id (pk, auto)  정수  , name  문자열  nn, age 정수 nn, city 문자열  nn
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,        
        name  TEXT NOT NULL,        
        age   INTEGER NOT NULL,        
        city  TEXT NOT NULL
       )    
''')
insert_emp = "insert into employees (name,age,city) values (?,?,?)"

#4.  insert_t, select, delete_t, update_t
# SQL 실행 (Cursor 객체의 execute() 메서드를 사용하여 INSERT, UPDATE 혹은 DELETE 문장을 DB 서버에 보냄)
def insert_employees(name,age,city):
    cursor.execute('insert into employees ( name, age,city) values ( ?,?,?)',(name,age,city) )
    conn.commit() # EXECUTE 문은 연결된 서버 명령

def  selectall_employees():
    cursor.execute('select   * from  employees' ) # 한줄 이상
    return cursor.fetchall() # select 결과를 리턴하겠다. fecthall은 리스트 객체를 반환 ->list

def update_employees(id, name, age, city):
    # id를 찾아서 name,age,city로 변경하겠다.
    cursor.execute('UPDATE employees SET name=?, age=?, city=? WHERE id=?', (name, age, city, id))
    conn.commit()
def  delete_employees(id):
    cursor.execute('DELETE FROM employees WHERE id=?', (id,))
    conn.commit()

#5. 실행 결과
#########insert

insert_employees('홍길동1', 21, '서울1')
insert_employees('홍길동2', 22, '서울2')
insert_employees('홍길동3', 23, '서울3')

#6. 출력
# print(selectall_employees())
# id 변경
# update_employees(1 ,'정길동', 35, '인천')
# print(selectall_employees())
# delete_employees(1,)
print(selectall_employees())