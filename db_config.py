#1
from app import app
#2
from flaskext.mysql import MySQL

mysql = MySQL()

#3
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'emp_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)