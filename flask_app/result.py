from flask import Flask, render_template
app = Flask(__name__)
@app.route('/result/<int:score>')
def result(score):
	return render_template('result.htm', marks = score)
if __name__ == '__main__':
	app.run(debug = True)
