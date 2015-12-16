import mysql.connector
from mysql.connector import errorcode
import configparser


def run_create_sql():
	database_connector, cursor = connect_to_server()
	with open('create.sql', 'r') as c_file:
		commands = c_file.read()
	split_commands = commands.split(";")
	try:
		for command in split_commands:
			cursor.execute(command)
	except mysql.connector.Error as err:
			print(err)


def connect_to_server():
	try:
		database_connector = mysql.connector.connect(user='root', password="12345", host="127.0.0.1")
		cursor = database_connector.cursor()
		return database_connector, cursor
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("default")