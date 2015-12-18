from _010_add_new_donor import *
from _011_donor_inputs import *
from _020_add_new_event import *
from _021_event_inputs import *
import csv
from sql_helper import *


modified_donor = Donor()
modified_event = Event()
donor_selector = lambda: input("Please select which data you want to change by entering the corresponding number from the menu here (except 7 and 13): ")
event_selector = lambda: input("Please select which data you want to change by entering the corresponding number from the menu here (except10): ")
id_input = lambda: input("Please enter the ID that you want to find: ")


def modify_data(file_path, id_index_in_row, pure_data, header, string_name):
	"""

	:param file_path:
	:param id_index_in_row:
	:param pure_data:
	:param header:
	:param string_name:
	:return:
	"""
	id = id_input()
	id_in_file = False
	all_data_without_id_row = []
	all_data_without_id_row.append(header)
	modified_row = []
	for row in pure_data:
		if id != row[id_index_in_row]:
			all_data_without_id_row.append(row)
	for row in pure_data:
		if id == row[id_index_in_row]:
			id_in_file = True
			for index, each_element_in_header, each_data_in_founded_row in zip(range(1, len(header) + 1), header, row):
				print(index, each_element_in_header, ":", each_data_in_founded_row)
				modified_row.append(each_data_in_founded_row)
	if not id_in_file:
		print("Not found! Try again!")
		modify_data(file_path, id_index_in_row, pure_data, header, string_name)
	if string_name == "Donor":
		modify_donor_csv(file_path, all_data_without_id_row, modified_row)
	if string_name == "Event":
		modify_event_csv(file_path, all_data_without_id_row, modified_row)


def modify_donor_csv(file_path, all_data_without_id_row, modified_row):
	selected_number = donor_selector()
	while donor_selector() not in ['1', '2', '3', '4', '5', '6', '8', '9', '10', '11', '12']:
		donor_selector()
	if selected_number == "1":
		modified_donor.get_first_name()
		modified_row[0] = modified_donor.first_name
	if selected_number == "2":
		modified_donor.get_last_name()
		modified_row[1] = modified_donor.last_name
	if selected_number == "3":
		modified_donor.get_weight()
		modified_row[2] = modified_donor.weight
	if selected_number == "4":
		modified_donor.get_gender()
		modified_row[3] = modified_donor.gender
	if selected_number == "5":
		modified_donor.get_date_of_birth()
		modified_row[4] = modified_donor.date_of_birth
	if selected_number == "6":
		modified_donor.get_donation_date()
		modified_row[5] = modified_donor.donation_date
	if selected_number == "8":
		modified_donor.get_id_number()
		while id_is_exist(modified_donor.id_number):
			modified_donor.get_id_number()
		modified_row[7] = modified_donor.id_number
	if selected_number == "9":
		modified_donor.get_exp_date()
		modified_row[8] = modified_donor.get_exp_date()
	if selected_number == "10":
		modified_donor.get_blood_type()
		modified_row[9] = modified_donor.blood_type
	if selected_number == "11":
		modified_donor.get_email_address()
		modified_row[10] = modified_donor.email_address
	if selected_number == "12":
		modified_donor.get_mobile_number()
		modified_row[11] = modified_donor.mobile_number
	ask_write_to_file = input("Write to file? Press y otherwise press any key to back to the main menu: ")
	if ask_write_to_file == "y":
		write_modified_row_into_csv(file_path, all_data_without_id_row, modified_row)
	else:
		print("Bye")
		return False


def modify_event_csv(file_path, all_data_without_id_row, modified_row):
	selected_number = event_selector()
	while selected_number not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '11']:
		event_selector()
	if selected_number == "1":
		modified_event.generate_event_id()
		modified_row[0] = modified_event.event_id
	if selected_number == "2":
		modified_event.get_date_of_event()
		modified_row[1] = modified_event.date_of_event
	if selected_number == "3":
		modified_event.get_start_time()
		modified_row[2] = modified_event.start_time
	if selected_number == "4":
		modified_event.get_end_time()
		modified_row[3] = modified_event.end_time
	if selected_number == "5":
		modified_event.get_zip_code()
		modified_row[4] = modified_event.zip_code
	if selected_number == "6":
		modified_event.get_city()
		modified_row[5] = modified_event.city
	if selected_number == "7":
		modified_event.get_address()
		modified_row[6] = modified_event.address
	if selected_number == "8":
		modified_event.get_available_beds()
		modified_row[7] = modified_event.available_beds
	if selected_number == "9":
		modified_event.get_planned_donor_number()
		modified_row[8] = modified_event.planned_donors
	if selected_number == "11":
		modified_event.get_successful_donations()
		modified_row[10] = modified_event.successful_donations
	ask_write_to_file = input("Write to file? Press y otherwise press any key to back to the main menu: ")
	if ask_write_to_file == "y":
		write_modified_row_into_csv(file_path, all_data_without_id_row, modified_row)
	else:
		print("Bye")
		return False


def write_modified_row_into_csv(file_path, all_data_without_id_row, modified_row):
	with open(file_path, "w") as csv_file:
		csv_writer = csv.writer(csv_file)
		for row in all_data_without_id_row:
			csv_writer.writerow(row)
	with open(file_path, "a") as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(modified_row)
	return False


def modify_donor_sql(string_name, header):
	id = id_input()
	if not id_in_table(string_name, id):
			print("\nID not found! Please try again!")
			sleep(2), modify_donor_sql(string_name, header)
	database_connector, cursor = connect_to_server()
	cursor.execute("USE BloodDonationStorage")
	cursor.execute("SELECT * FROM {} WHERE Id_number = '{}'".format(string_name, id))
	selected_row = cursor.fetchall()
	for element in selected_row:
		for index, each_element_in_header, each_data_in_founded_row in zip(range(1, len(header) + 1), header, element):
				print(index, each_element_in_header, ":", each_data_in_founded_row)
	selected_number = donor_selector()
	while selected_number not in ['1', '2', '3', '4', '5', '6', '8', '9', '10', '11', '12']:
		donor_selector()
	if selected_number == "1":
		modified_donor.get_first_name()
		modify_donor_table = """UPDATE {} SET First_name = '{}'WHERE Id_number = '{}'""".format(string_name, modified_donor.first_name, id)
		cursor.execute(modify_donor_table)
		database_connector.commit()
	if selected_number == "2":
		modified_donor.get_last_name()
		modify_donor_table = """UPDATE {} SET Last_name = '{}'WHERE Id_number = '{}'""".format(string_name, modified_donor.last_name, id)
		cursor.execute(modify_donor_table)
		database_connector.commit()
	if selected_number == "3":
		modified_donor.get_weight()
		modify_donor_table = """UPDATE {} SET Weight = '{}'WHERE Id_number = '{}'""".format(string_name, modified_donor.weight, id)
		cursor.execute(modify_donor_table)
		database_connector.commit()
	if selected_number == "4":
		modified_donor.get_gender()
		modify_donor_table = """UPDATE {} SET Gender = '{}'WHERE Id_number = '{}'""".format(string_name, modified_donor.gender, id)
		cursor.execute(modify_donor_table)
		database_connector.commit()
	if selected_number == "5":
		modified_donor.get_date_of_birth()
		modify_donor_table = """UPDATE {} SET Date_of_birth = '{}'WHERE Id_number = '{}'""".format(string_name, modified_donor.date_of_birth, id)
		cursor.execute(modify_donor_table)
		database_connector.commit()
	if selected_number == "6":
		modified_donor.get_donation_date()
		modify_donor_table = """UPDATE {} SET Donation_date = '{}'WHERE Id_number = '{}'""".format(string_name, modified_donor.donation_date, id)
		cursor.execute(modify_donor_table)
		database_connector.commit()
	if selected_number == "8":
		modified_donor.get_id_number()
		while id_in_table(string_name, modified_donor.id_number):
			print("ID is already exist!")
			modified_donor.get_id_number()
		modify_donor_table = """UPDATE {} SET ID_number = '{}'WHERE Id_number = '{}'""".format(string_name, modified_donor.id_number, id)
		cursor.execute(modify_donor_table)
		database_connector.commit()
	if selected_number == "9":
		modified_donor.get_exp_date()
		modify_donor_table = """UPDATE {} SET Expiration_date = '{}'WHERE Id_number = '{}'""".format(string_name, modified_donor.exp_date, id)
		cursor.execute(modify_donor_table)
		database_connector.commit()
	if selected_number == "10":
		modified_donor.get_blood_type()
		modify_donor_table = """UPDATE {} SET Blood_type = '{}'WHERE Id_number = '{}'""".format(string_name, modified_donor.blood_type, id)
		cursor.execute(modify_donor_table)
		database_connector.commit()
	if selected_number == "11":
		modified_donor.get_email_address()
		modify_donor_table = """UPDATE {} SET Email_address = '{}'WHERE Id_number = '{}'""".format(string_name, modified_donor.email_address, id)
		cursor.execute(modify_donor_table)
		database_connector.commit()
	if selected_number == "12":
		modified_donor.get_mobile_number()
		modify_donor_table = """UPDATE {} SET Mobile_number = '{}'WHERE Id_number = '{}'""".format(string_name, modified_donor.mobile_number, id)
		cursor.execute(modify_donor_table)
		database_connector.commit()


def modify_event_sql(string_name, header):
	id = id_input()
	if not id_in_table(string_name, id):
		print("\nID not found! Please try again!")
		sleep(2), modify_event_sql(string_name, header)
	database_connector, cursor = connect_to_server()
	cursor.execute("USE BloodDonationStorage")
	cursor.execute("SELECT * FROM {} WHERE Id_number = '{}'".format(string_name, id))
	selected_row = cursor.fetchall()
	for element in selected_row:
		for index, each_element_in_header, each_data_in_founded_row in zip(range(1, len(header) + 1), header, element):
				print(index, each_element_in_header, ":", each_data_in_founded_row)
	selected_number = event_selector()
	while selected_number not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '11']:
		event_selector()
	if selected_number == "1":
		modified_event.generate_event_id()
		modify_event_table = """UPDATE {} SET ID_number = '{}'WHERE Id_number = '{}'""".format(string_name, modified_event.event_id, id)
		cursor.execute(modify_event_table)
		database_connector.commit()
		database_connector.commit()
	if selected_number == "2":
		modified_event.get_date_of_event()
		modify_event_table = """UPDATE {} SET Date_of_Event = '{}'WHERE Id_number = '{}'""".format(string_name, modified_event.date_of_event, id)
		cursor.execute(modify_event_table)
		database_connector.commit()
	if selected_number == "3":
		modified_event.get_start_time()
		modify_event_table = """UPDATE {} SET Start_time = '{}'WHERE Id_number = '{}'""".format(string_name, modified_event.start_time, id)
		cursor.execute(modify_event_table)
		database_connector.commit()
	if selected_number == "4":
		modified_event.get_end_time()
		modify_event_table = """UPDATE {} SET End_time = '{}'WHERE Id_number = '{}'""".format(string_name, modified_event.end_time, id)
		cursor.execute(modify_event_table)
		database_connector.commit()
	if selected_number == "5":
		modified_event.get_zip_code()
		modify_event_table = """UPDATE {} SET Zip_code = '{}'WHERE Id_number = '{}'""".format(string_name, modified_event.zip_code, id)
		cursor.execute(modify_event_table)
		database_connector.commit()
	if selected_number == "6":
		modified_event.get_city()
		modify_event_table = """UPDATE {} SET City = '{}'WHERE Id_number = '{}'""".format(string_name, modified_event.city, id)
		cursor.execute(modify_event_table)
		database_connector.commit()
	if selected_number == "7":
		modified_event.get_address()
		modify_event_table = """UPDATE {} SET Address = '{}'WHERE Id_number = '{}'""".format(string_name, modified_event.address, id)
		cursor.execute(modify_event_table)
		database_connector.commit()
	if selected_number == "8":
		modified_event.get_available_beds()
		modify_event_table = """UPDATE {} SET Available_beds = '{}'WHERE Id_number = '{}'""".format(string_name, modified_event.available_beds, id)
		cursor.execute(modify_event_table)
		database_connector.commit()
	if selected_number == "9":
		modified_event.get_planned_donor_number()
		modify_event_table = """UPDATE {} SET Planned_donors = '{}'WHERE Id_number = '{}'""".format(string_name, modified_event.planned_donors, id)
		cursor.execute(modify_event_table)
		database_connector.commit()
	if selected_number == "11":
		modified_event.get_successful_donations()
		modify_event_table = """UPDATE {} SET Successful_donations = '{}'WHERE Id_number = '{}'""".format(string_name, modified_event.successful_donations, id)
		cursor.execute(modify_event_table)
		database_connector.commit()

