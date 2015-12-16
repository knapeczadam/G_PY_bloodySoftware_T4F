from csv_helper import *
from setup_database import connect_to_server
import mysql.connector
from time import sleep


def delete_data_from_file(file_path, id_index_in_row, pure_data, header, string_name):
	"""
	:return:
	"""
	id_input = input("\nPlease enter the {}'s id that you want to delete: ".format(string_name))
	id_in_file = False
	all_data_without_id_row = []
	all_data_without_id_row.append(header)
	for row in pure_data:
		if id_input != row[id_index_in_row]:
			all_data_without_id_row.append(row)
	for row in pure_data:
		if id_input == row[id_index_in_row]:
			id_in_file = True
	if id_in_file:
		are_you_sure = input("Are you sure? If yes, press y otherwise press any key to go back to the main menu: ")
		if are_you_sure == "y":
			with open(file_path, "w") as csv_file:
				csv_writer = csv.writer(csv_file)
				for row in all_data_without_id_row:
					csv_writer.writerow(row)
			print("Successful delete! Back to the main menu...")
	if not id_in_file:
		print("\nID not found! Please try again!")
		delete_data_from_file(file_path, id_index_in_row, pure_data, header, string_name)


def delete_data_from_sql_file(string_name):
	database_connector, cursor = connect_to_server()
	cursor.execute("USE BloodDonationStorage")
	cursor.execute("SELECT ID_number FROM {}".format(string_name))
	pure_data = cursor.fetchall()
	id_input = input("\nPlease enter the {}'s id that you want to delete: ".format(string_name))
	try:
		ids = [id[0] for id in pure_data]
		if id_input not in ids:
			print("\nID not found! Please try again!")
			sleep(2)
			return delete_data_from_sql_file(string_name)
		delete_row = """DELETE FROM {}
		WHERE ID_number = '{}'""".format(string_name, id_input)
		cursor.execute(delete_row)
		database_connector.commit()
		print("Successful delete! Back to the main menu...")
		sleep(2)
	except Exception as err:
		print(err)
