from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap

import mysql.connector as sql
app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def home():
	return render_template('home.htm')
@app.route('/registration')
def new_student():
	return render_template('registration.htm')
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
	if request.method == 'POST':
		try:
			EmpID = request.form['EmpID']
			EmpName = request.form['EmpName']
			EmpGender = request.form['EmpGender']
			EmpPhone = request.form['EmpPhone']
			EmpBDate = request.form['EmpBDate']
			with sql.connect(host="localhost", user="flask", password="ubuntu", database="Week12_DB") as con:
				cur = con.cursor()
				cmd = "INSERT INTO employees (EmpID, EmpName, EmpGender, EmpPhone, EmpBDate) VALUES ('{0}','{1}','{2}','{3}', '{4}')".format(EmpID, EmpName, EmpGender, EmpPhone, EmpBDate)
				cur.execute(cmd)
				con.commit()
				msg = "Record successfully added"
		except:
			con.rollback()
			msg = "error in insert operation"
		finally:
			return render_template("result.htm", msg = msg)
			con.close()
@app.route('/information')
def list():
	with sql.connect(host="localhost", user="flask", password="ubuntu", database="Week12_DB") as con:
		cur = con.cursor()
		cur.execute("select * from employees")
		rows = cur.fetchall();
	return render_template("list.htm",rows = rows)
if __name__ == '__main__':
	app.run(debug = True)
