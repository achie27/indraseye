from mysql.connector import connection


def connect():
	config = {
	  'user': 'root',
	  'password': 'root',
	  'host': '127.0.0.1',
	  'database': 'hasura',
	  'raise_on_warnings': True,
	}
	conn = connection.MySQLConnection(**config)
	print("succesfully connected to database")
	# cursor = conn.cursor()
	return conn

