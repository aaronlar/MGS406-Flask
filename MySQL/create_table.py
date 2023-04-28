import mysql.connector as sql

conn = sql.connect(host="localhost", user="flask", password="ubuntu", database="Week12_DB")
cur = conn.cursor()

cmd = "CREATE TABLE employees (\
    EmpID VARCHAR(30) NOT NULL PRIMARY KEY, \
    EmpName VARCHAR(30) NOT NULL,\
    EmpGender VARCHAR(30), \
    EmpPhone VARCHAR(30), \
    EmpBDate VARCHAR(30))"

cur.execute(cmd)
conn.close()
