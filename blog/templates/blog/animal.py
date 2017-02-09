 #!/usr/bin/python
#  -*- coding: utf-8 -*-

import sqlite3

# DB 연결
db = sqlite3.connect("test.db")
cursor = db.cursor()

datas = [(1, "cheetah"), (2, "puma"), (3, "leopard")]

# 테이블 생성
cursor.execute("create table animal (no, name)")

# 데이터 INSERT
cursor.executemany("insert into animal values (?, ?)", datas)

# 최종 INSERT된 rowid 출력
print ('Last rowid: ' + str(cursor.lastrowid))
# Row count 출력
print ('Row count: ' + str(cursor.rowcount))


# 쿼리
cursor.execute("select * from animal")
for row in cursor:
    print (row[1])

cursor.execute("update animal set name='jaguar' where no=3");

cursor.execute("select * from animal")
print (cursor.fetchall())

cursor.execute("select * from animal where no=1")
row = cursor.fetchone()
print ('No 1 is ' + row[1]);

# 종료
cursor.close()

db.commit()
db.close()
