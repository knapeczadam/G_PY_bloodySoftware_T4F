from _010_add_new_donor import *
from _011_donor_inputs import *
from _020_add_new_event import *
from _021_event_inputs import *
import csv


modified_donor = Donor()
modified_event = Event()


def modify_data(file_path, id_index_in_row, pure_data, header, string_name):
	"""
	
	:param file_path: 
	:param id_index_in_row: 
	:param pure_data: 
	:param header: 
	:param string_name: 
	:return: 
	"""
	id_input = input("Please enter the ID of the {} that you want to find: ".format(string_name))
	id_in_file = False
	all_data_without_id_row = []
	all_data_without_id_row.append(header)
	modified_row = []
	for row in pure_data:
		if id_input != row[id_index_in_row]:
			all_data_without_id_row.append(row)
	for row in pure_data:
		if id_input == row[id_index_in_row]:
			id_in_file = True
			for index, each_element_in_header, each_data_in_founded_row in zip(range(1, len(header) + 1), header, row):
				print(index, each_element_in_header, ":", each_data_in_founded_row)
				modified_row.append(each_data_in_founded_row)
	if not id_in_file:
		print("Not found! Try again!")
		modify_data(file_path, id_index_in_row, pure_data, header, string_name)
	if string_name == "Donor":
		donor_seletor(file_path, all_data_without_id_row, modified_row)
	if string_name == "Event":
		event_selector(file_path, all_data_without_id_row, modified_row)


def donor_seletor(file_path, all_data_without_id_row, modified_row):
	selector = input("Please select which data you want to change by entering the corresponding number from the menu here (except 7 and 13): ")
	while selector not in ['1', '2', '3', '4', '5', '6', '8', '9', '10', '11', '12']:
		selector = input("Please select which data you want to change by entering the corresponding number from the menu here (except 7 and 13): ")
	if selector == "1":
		modified_donor.get_first_name()
		modified_row[0] = modified_donor.first_name
	if selector == "2":
		modified_donor.get_last_name()
		modified_row[1] = modified_donor.last_name
	if selector == "3":
		modified_donor.get_weight()
		modified_row[2] = modified_donor.weight
	if selector == "4":
		modified_donor.get_gender()
		modified_row[3] = modified_donor.gender
	if selector == "5":
		modified_donor.get_date_of_birth()
		modified_row[4] = modified_donor.date_of_birth
	if selector == "6":
		modified_donor.get_donation_date()
		modified_row[5] = modified_donor.donation_date
	if selector == "8":
		modified_donor.get_id_number()
		while id_is_exist(modified_donor.id_number):
			modified_donor.get_id_number()
		modified_row[7] = modified_donor.id_number
	if selector == "9":
		modified_donor.get_exp_date()
		modified_row[8] = modified_donor.get_exp_date()
	if selector == "10":
		modified_donor.get_blood_type()
		modified_row[9] = modified_donor.blood_type
	if selector == "11":
		modified_donor.get_email_address()
		modified_row[10] = modified_donor.email_address
	if selector == "12":
		modified_donor.get_mobile_number()
		modified_row[11] = modified_donor.mobile_number
	ask_write_to_file = input("Write to file? Press y otherwise press any key to back to the main menu: ")
	if ask_write_to_file == "y":
		write_modified_row_to_file(file_path, all_data_without_id_row, modified_row)
	else:
		print("Bye")
		return False


def event_selector(file_path, all_data_without_id_row, modified_row):
	selector = input("Please select which data you want to change by entering the corresponding number from the menu here (except10): ")
	while selector not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '11']:
		selector = input("Please select which data you want to change by entering the corresponding number from the menu here (except10): ")
	if selector == "1":
		modified_event.generate_event_id()
		modified_row[0] = modified_event.event_id
	if selector == "2":
		modified_event.get_date_of_event()
		modified_row[1] = modified_event.date_of_event
	if selector == "3":
		modified_event.get_start_time()
		modified_row[2] = modified_event.start_time
	if selector == "4":
		modified_event.get_end_time()
		modified_row[3] = modified_event.end_time
	if selector == "5":
		modified_event.get_zip_code()
		modified_row[4] = modified_event.zip_code
	if selector == "6":
		modified_event.get_city()
		modified_row[5] = modified_event.city
	if selector == "7":
		modified_event.get_address()
		modified_row[6] = modified_event.address
	if selector == "8":
		modified_event.get_available_beds()
		modified_row[7] = modified_event.available_beds
	if selector == "9":
		modified_event.get_planned_donor_number()
		modified_row[8] = modified_event.planned_donors
	if selector == "11":
		modified_event.get_successful_donations()
		modified_row[10] = modified_event.successful_donations
	ask_write_to_file = input("Write to file? Press y otherwise press any key to back to the main menu: ")
	if ask_write_to_file == "y":
		write_modified_row_to_file(file_path, all_data_without_id_row, modified_row)
	else:
		print("Bye")
		return False


def write_modified_row_to_file(file_path, all_data_without_id_row, modified_row):
	with open(file_path, "w") as csv_file:
		csv_writer = csv.writer(csv_file)
		for row in all_data_without_id_row:
			csv_writer.writerow(row)
	with open(file_path, "a") as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(modified_row)
	return False
