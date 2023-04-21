@app.route('/enternew')
def new_student():
	return render_template('student.html')
