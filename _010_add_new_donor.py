from _011_donor_inputs import Donor
from datetime import datetime
from os import path
import time
import csv
import os

ESC = ["exit"]

user = Donor()


def call_get_donor_inputs():
	"""

	:return:
	"""
	get_data_from_user_or_exit(user.get_first_name(), user.first_name)
	get_data_from_user_or_exit(user.get_last_name(), user.last_name)
	get_data_from_user_or_exit(user.get_weight(), user.weight)
	user_requirements()
	get_data_from_user_or_exit(user.get_gender(), user.gender)
	get_data_from_user_or_exit(user.get_date_of_birth(), user.date_of_birth)
	user_requirements()
	get_data_from_user_or_exit(user.get_donation_date(), user.donation_date)
	user_requirements()
	get_data_from_user_or_exit(user.get_sickness(), user.sickness)
	user_requirements()
	get_data_from_user_or_exit(user.get_id_number(), user.id_number)
	get_data_from_user_or_exit(user.get_exp_date(), user.exp_date)
	user_requirements()
	get_data_from_user_or_exit(user.get_blood_type(), user.blood_type)
	get_data_from_user_or_exit(user.get_email_address(), user.email_address)
	get_data_from_user_or_exit(user.get_mobile_number(), user.mobile_number)


def write_donor_data_in_file():
	"""

	:return:
	"""
	donor_date = [user.first_name,\
				  user.last_name,\
				  user.weight,\
				  user.gender,\
				  user.date_of_birth,\
				  user.donation_date,\
				  user.sickness,\
				  user.id_number,\
				  user.exp_date,\
				  user.blood_type,\
				  user.email_address,\
				  user.mobile_number]
	if not (path.isfile("Data\donors.csv")):
		f = open("Data\donors.csv", 'w')
		f.close()
	data = []
	with open("Data\donors.csv") as csvfile_read:
		csvreader = csv.reader(csvfile_read, delimiter=",")
		for row in csvreader:
			if row:
				data.append(row)
	csvfile_read.close()
	dicta = {}
	x = 1
	for elements in data:
		dicta[x] = elements
		x += 1
	print("The donor's data has been recorded.")
	with (open("Data\donors.csv", 'w')) as writer:
		csvwriter = csv.writer(writer, delimiter=",")
		for word in dicta:
			csvwriter.writerow(dicta[word])
	with open("Data\donors.csv", "a") as csvfile_write:
		csvwriter = csv.writer(csvfile_write, delimiter=',')
		csvwriter.writerow(donor_date)
		print("New donor:", donor_date)


def user_requirements():
	"""

	:param user_input:
	:return:
	"""
	if user.weight is not None:
		if int(user.weight) <= 50:
			weight_message = "Donors are only accepted above 50 kgs.\
			\nThe program has ended because of not suitable donor."
			user.weight = None
			clean_and_back_to_the_main_menu(weight_message)
	if user.date_of_birth is not None and user.date_of_birth not in ESC:
		if (datetime.now() - datetime.strptime(user.date_of_birth, "%Y.%m.%d")).days // 365 < 18:
			age_message = "Donors are only accepted above 18 years.\
			\nThe program has ended because of not suitable donor."
			user.date_of_birth = None
			clean_and_back_to_the_main_menu(age_message)
	if user.donation_date is not None and user.donation_date != "" and user.donation_date not in ESC:
			if (datetime.now() - datetime.strptime(user.donation_date, "%Y.%m.%d")).days <= 90:
				donation_message = "Donors can only give blood once in every 3 months.\
				\nThe program has ended because of not suitable donor."
				user.donation_date = None
				clean_and_back_to_the_main_menu(donation_message)
	if user.sickness is not None:
		if user.sickness.lower() == "y":
			sickness_message = "The program has ended because of not suitable donor."
			user.sickness = None
			clean_and_back_to_the_main_menu(sickness_message)
	if user.exp_date is not None and user.exp_date not in ESC:
		if datetime.strptime(user.exp_date, "%Y.%m.%d") < datetime.now():
			expiration_message = "The donor's ID is expired! Program is shutting down..."
			user.exp_date = None
			clean_and_back_to_the_main_menu(expiration_message)


# def find_existing_id(id_numer):
# 	"""
#
# 	:param id_numer:
# 	:return:
# 	"""
# 	data = []
# 	with open("Data\donors.csv") as csvfile_read:
# 		csvreader = csv.reader(csvfile_read, delimiter=",")
# 		for row in csvreader:
# 			if row:
# 				data.append(row)
# 	csvfile_read.close()
# 	dicta = {}
# 	x = 1
# 	for elements in data:
# 		dicta[x] = elements
# 		x += 1
# 	find_id = 0
# 	if id_numer:
# 		for key in dicta:
# 			for element in dicta[key]:
# 				if element == id_numer:
# 					find_id += key


def get_data_from_user_or_exit(get_something, user_string_input):
	"""

	:param user_input:
	:param get_something:
	:return:
	"""
	if user_string_input.lower() in ESC:
		exit_message = "Bye"
		clean_and_back_to_the_main_menu(exit_message)


def clean_and_back_to_the_main_menu(message):
	"""

	:param message:
	:return:
	"""
	os.system("CLS")
	print(message)
	# time.sleep(3)
	from main import menu
	menu()