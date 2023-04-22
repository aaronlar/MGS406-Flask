import sqlite3
conn = sqlite3.connect('database.db')

print("Opened database successfully")

conn.execute('CREATE TABLE employee (EmpID TEXT, EmpName TEXT, EmpGender TEXT, EmpPhone TEXT, EmpBDate TEXT)')

print("Table created successfully")

conn.close()
