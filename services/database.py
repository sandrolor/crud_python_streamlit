from mysql.connector import (connection)
	
db_connection = connection.MySQLConnection(host='127.0.0.1', user='root', password='', database='crud_python_db')
cursor = db_connection.cursor()
