import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
	html = ''' <img src='{}'/>'''
	html = html.format(flask.url_for('static',filename='cat.jpeg'))
	return html

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
	return flask.render_template('hello.html',name=name)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')