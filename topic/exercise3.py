import flask

app = flask.Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if flask.request.method == 'POST':
        if valid_login(flask.request.form.get('username'),
                       flask.request.form.get('password')):
            return log_the_user_in(flask.request.form.get('username'))
        else:
            error = 'Invalid username or password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return flask.render_template('login.html', error=error)

def valid_login(username=None,password=None):    
    return True if username and password else False

def log_the_user_in(username=None):
    return 'Hello {}'.format(username)

if __name__ == '__main__':
    app.run(debug=True)