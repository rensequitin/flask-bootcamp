import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
	html = '''<a href='{}'>greet</a><br>
			<a href='{}'>banana</a> '''
	html = html.format(flask.url_for('greet'),
					   flask.url_for('show_fruit', name='banana'))
	return html

@app.route('/say_hi')
def greet():
	return 'Hello World'

@app.route('/fruits/<name>')
def show_fruit(name):
	html = 'I like this fruit' + name
	return html

@app.route('/magic/<int:number>')
def show_magic(number):
	html = """
		 The correct answer is:
		 {}"""
	html = html.format(number)
	html = html.replace('\n','</br>')
	return html

if __name__ == '__main__':
	app.run(debug=True)