from _010_add_new_donor import *
from _011_donor_inputs import *
from _020_add_new_event import *
from _021_event_inputs import *
import time
import csv

user = Donor()
event = Event()


def modify_data(file, given_id, file_name, first_row, file_name_string):


	donor_id = input("Please enter the ID of the {} that you want to find: ".format(file_name_string))
	file_datas_without_modified_data = []
	if file_name_string == "Donor":
		file_datas_without_modified_data.append(first_row)
	if file_name_string == "Event":
		file_datas_without_modified_data.append(first_row)

	modified_data = []
	for row in file:
		if donor_id != row[given_id]:
			file_datas_without_modified_data.append(row)

	for row in file:
		if donor_id == row[given_id]:
			for element in row:
				modified_data.append(element)
			for index, each_element_in_first_row, each_data_in_file in zip(range(1, len(first_row) + 1), first_row, row):
				print(index, each_element_in_first_row, ":", each_data_in_file)
			# print(file_datas_without_modified_data)
			# print(modified_data)
			# time.sleep(5)
	if file_name_string == "Donor":
		donor_seletor(file_name, file_datas_without_modified_data, modified_data)
	if file_name_string == "Event":
		event_selector(file_name, file_datas_without_modified_data, modified_data)


def donor_seletor(file_name, file_datas_without_modified_data, modified_data):
	selecetor = input("Please select which data you want to change by entering the corresponding number from the menu here (except 7 and 13): ")

	if selecetor == "1":
		user.get_first_name()
		modified_data[0] = user.first_name
	if selecetor == "2":
		user.get_last_name()
		modified_data[1] = user.last_name
	if selecetor == "3":
		user.get_weight()
		modified_data[2] = user.weight
	if selecetor == "4":
		user.get_gender()
		modified_data[3] = user.gender
	if selecetor == "5":
		user.get_date_of_birth()
		modified_data[4] = user.date_of_birth
	if selecetor == "6":
		user.get_donation_date()
		modified_data[5] = user.donation_date
	if selecetor == "8":
		find_existing_id(user.get_id_number(), user.id_number)
		modified_data[7] = user.id_number
	if selecetor == "9":
		user.get_exp_date()
		modified_data[8] = user.get_exp_date()
	if selecetor == "10":
		user.get_blood_type()
		modified_data[9] = user.blood_type
	if selecetor == "11":
		user.get_email_address()
		modified_data[10] = user.email_address
	if selecetor == "12":
		user.get_mobile_number()
		modified_data[11] = user.mobile_number
	modification_is_yes = input("write to file? (y): ")
	while modification_is_yes != "y":
		modification_is_yes = input("write to file? (y): ")
	if modification_is_yes == "y":
		write_modified_data_to_file(file_name, file_datas_without_modified_data, modified_data)


def event_selector(file_name, file_datas_without_modified_data, modified_data):
	selecetor = input("Please select which data you want to change by entering the corresponding number from the menu here ( except10): ")

	if selecetor == "1":
		event.generate_event_id()
		modified_data[0] = event.event_id
	if selecetor == "2":
		event.get_date_of_event()
		modified_data[1] = event.date_of_event
	if selecetor == "3":
		event.get_start_time()
		modified_data[2] = event.start_time
	if selecetor == "4":
		event.get_end_time()
		modified_data[3] = event.end_time
	if selecetor == "5":
		event.get_zip_code()
		modified_data[4] = event.zip_code
	if selecetor == "6":
		event.get_city()
		modified_data[5] = event.city
	if selecetor == "7":
		event.get_address()
		modified_data[6] = event.address
	if selecetor == "8":
		event.get_available_beds()
		modified_data[7] = event.available_beds
	if selecetor == "9":
		event.get_planned_donor_number()
		modified_data[8] = event.planned_donors
	if selecetor == "11":
		event.get_successful_donations()
		modified_data[10] = event.successful_donations
	modification_is_yes = input("write to file? (y): ")
	while modification_is_yes != "y":
		modification_is_yes = input("write to file? (y): ")
	if modification_is_yes == "y":
		write_modified_data_to_file(file_name, file_datas_without_modified_data, modified_data)


def write_modified_data_to_file(file_name, file_datas_without_modified_data, modified_data):
		with open(file_name, "w") as csv_file:
			csv_writer = csv.writer(csv_file)
			for row in file_datas_without_modified_data:
				csv_writer.writerow(row)

		with open(file_name, "a") as csv_file:
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow(modified_data)


