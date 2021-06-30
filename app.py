from logging import shutdown
import mysql.connector
from flask import Flask
import atexit


app = Flask(__name__)


@app.route('/')
def coffee():
  mydb = mysql.connector.connect(
    host="db",
    user="root",
    password="p@ssw0rd1",
    database="inventory"
  )
  return "It's time to coffee"


@app.route("/shutdown", methods = ['POST'])
def shutdown_server():
	print("Shutdown context hit with POST!")
	if request.form.get('username') and request.form.get('password'):
		print('Got username: {} and password: {}'.format(request.form.get('username'),request.form.get('password')))
		if request.form.get('username') != user:
			return 'The username or password is incorrect!'

		if request.form.get('password') != pwd:
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

@app.route('/initdb')
def db_init():
  mydb = mysql.connector.connect(
    host="db",
    user="root",
    password="p@ssw0rd1"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP DATABASE IF EXISTS inventory")
  cursor.execute("CREATE DATABASE inventory")
  cursor.close()

  mydb = mysql.connector.connect(
    host="db",
    user="root",
    password="p@ssw0rd1",
    database="inventory"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP TABLE IF EXISTS widgets")
  cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
  cursor.close()

  return 'Here is nothing to do'

if __name__ == "__main__":
  app.run(host ='0.0.0.0', threaded=True)
shutdown
