from flask import Flask, request, render_template

user = 'admin'
pwd = 'Start!123'

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
	return "Welcome to the flask world!"
@app.route("/login/", methods=['POST', 'GET'])
def login():
    message = ''
    if request.method == 'POST':
	username = request.form.get('username') 
	password = request.form.get('password')

    if username == 'root' and password == 'pass':
	message = "Correct username and password"
    else:
	message = "Wrong username or password"

    return render_template('login.html', message=message)

@app.route("/shutdown", methods = ['GET', 'POST'])
def shutdown_server():
	print("Shutdown context hit with POST!")
	if request.args.get('username') and request.args.get('password'):
		print('Got username: {} and password: {}'.format(request.args.get('username'),request.args.get('password')))
		if request.args.get('username') != user:
			return 'The username or password is incorrect!'

		if request.args.get('password') != pwd:
			return 'The username or password is incorrect!'

		print("It seems to be valid, the server is shutting down!")
		shutdown = request.environ.get('werkzeug.server.shutdown')
		if shutdown is None:
			raise RuntimeError('The function is unavailable!')
		else:
			shutdown()
			return "THe server is shutting down!"

	else:
		return 'You need authorization to shut the server down!'

if __name__ == '__main__':
	app.run(port = 8081, host = '0.0.0.0', debug = True)
