import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
	link_1 = 'i0p1bmr0EmE'
	link_2 = 'rRzxEiBLQCA'
	link_3 = 'V2hlQkVJZhE'
	html = '''<a href='{}'>Video 1</a><br>
			  <a href='{}'>Video 2</a></br>
			  <a href='{}'>Video 3</a>'''
	html = html.format(flask.url_for('show_video', url=link_1),
					   flask.url_for('show_video', url=link_2),
					   flask.url_for('show_video', url=link_3))
	return html

@app.route('/video/<url>')
def show_video(url):
	html = '''<iframe width="854" height="480"
			   src="https://www.youtube.com/embed/{}"
			   frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>'''
	html = html.format(url)
	return html

if __name__ == '__main__':
	app.run(debug=True)