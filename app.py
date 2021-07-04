import mysql.connector
from flask import Flask


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

@app.route('/quit')
def quit():
    shutdown_hook = request.environ.get('werkzeug.server.shutdown')
    if shutdown_hook is not None:
         shutdown_hook()
         return "Bye"
    return "No shutdown hook"
if __name__ == "__main__":
  app.run(host ='0.0.0.0')
