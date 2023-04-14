from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
	return 'Hello World'
@app.route('/flask')
def hello_flask():
	return 'Hello Flask'
@app.route('/python/')
def hello_python():
	return 'Hello Python'
@app.route('/hello/<name>')
def hello_name(name):
	return 'Hello {0}!'.format(name)
@app.route('/blog/<int:postID>')
def show_blog(postID):
	return 'Blog Number {0} '.format(postID)
@app.route('/rev/<float:revNo>')
def revision(revNo):
	return 'Revision Number {0} '.format(revNo)
if __name__ == "__main__":
	app.run()
