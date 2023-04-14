from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the System'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'Buffalo$':
            return redirect(url_for('login_success'))
        else:
            return redirect(url_for('rejection'))
    return render_template('login.html')

@app.route('/login_success/')
def login_success():
    return 'Login Successful, Welcome Admin'

@app.route('/rejection/')
def rejection():
    return 'Login Failed, Please Try Again'

if __name__ == '__main__':
    app.run(debug=True)
