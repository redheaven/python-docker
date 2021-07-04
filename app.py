from flask import Flask, request

user = ''
pwd = ''

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
	return "Welcome world!"

@app.route("/shutdown", methods = ['GET', 'POST'])
def shutdown_server():
	print("Shutdown context hit with POST!")
	shutdown()

if __name__ == '__main__':
	app.run(port = 8081, host = '0.0.0.0', debug = True)
