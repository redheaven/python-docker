from flask import Flask, request

user = 'admin'
pwd = 'Start!123'

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
	return "Welcome to the flask world!"

@app.route("/shutdown", methods = ['GET', 'POST'])
def shutdown_server():
	print("Shutdown context hit with POST!")
	shutdown()
	return "THe server is shutting down!"

if __name__ == '__main__':
	app.run(port = 8081, host = '0.0.0.0', debug = True)
