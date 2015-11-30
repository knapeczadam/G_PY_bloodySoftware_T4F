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
	get_data_from_user_or_exit(find_existing_id(user.get_id_number()), user.id_number)
	get_data_from_user_or_exit(user.get_exp_date(), user.exp_date)
	user_requirements()
	get_data_from_user_or_exit(user.get_blood_type(), user.blood_type)
	get_data_from_user_or_exit(user.get_email_address(), user.email_address)
	get_data_from_user_or_exit(user.get_mobile_number(), user.mobile_number)


def write_donor_data_in_file():
	"""

	:return:
	"""
	donor_data = [
		user.first_name,
		user.last_name,
		user.weight,
		user.gender,
		user.date_of_birth,
		user.donation_date,
		user.sickness,
		user.id_number,
		user.exp_date,
		user.blood_type,
		user.email_address,
		user.mobile_number
	]

	first_row = [
		"First name",
		"Last name",
		"Weight",
		"Gender",
		"Date of birth",
		"Donation date",
		"Sickness",
		"ID number",
		"Expiration date",
		"Blood type",
		"Email address",
		"Mobile number"
	]

	csv_is_empty = True

	with open("Data\donors.csv", "r") as donors_csv:
		first_row_reader = csv.reader(donors_csv)
		for row in first_row_reader:
			if len(row) > 0:
				csv_is_empty = False

	if csv_is_empty:
		with open("Data\donors.csv", "w") as donors_csv:
			first_row_writer = csv.writer(donors_csv)
			first_row_writer.writerow(first_row)

	with open("Data\donors.csv", "a") as donors_csv:
		append_donor_data = csv.writer(donors_csv)
		append_donor_data.writerow(donor_data)

	age = (datetime.now() - datetime.strptime(user.date_of_birth, "%Y.%m.%d")).days // 365

	print("\n")
	print(
		"New donor has been added: ",
		"\n%s, %s" % (donor_data[0], donor_data[1]),
		"\n%skg" % donor_data[2],
		"\n%s, %s years old" % (donor_data[5], age),
		"\n%s" % donor_data[11]
	)
	print("\n")

	exit_input = input("If you want to exit the program press 'Y',"
	                    "\notherwise press 'Enter' to go back to the the main menu!")
	exit_lower = exit_input.lower()

	if exit_lower == "y":
		exit()
	else:
		clean_and_back_to_the_main_menu("Going back to the main menu...")


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


def find_existing_id(get_id_number):
	data_in_donors_csv = []
	with open("Data\donors.csv", "r") as donors_csv:
		csv_reader = csv.reader(donors_csv)
		for row in csv_reader:
			data_in_donors_csv.append(row)
	id_is_exist = 0
	for row in data_in_donors_csv:
		if len(row) != 0:
			if row[7] == user.id_number:
				print("ID is already exist!")
				id_is_exist += 1
				find_existing_id(user.get_id_number())
	if id_is_exist == 0:
		return True


def get_data_from_user_or_exit(get_something, user_string_input):
	"""

	:param user_input:
	:param get_something:
	:return:
	"""
	if user_string_input is not None:
		if user_string_input.lower() in ESC:
			exit_message = "Bye"
			clean_and_back_to_the_main_menu(exit_message)


def if_csv_is_not_exist():
	"""

	:return:
	"""
	if not (path.isfile("Data\donors.csv")):
		donors_csv = open("Data\donors.csv", 'w')
		donors_csv.close()


def clean_and_back_to_the_main_menu(message):
	"""

	:param message:
	:return:
	"""
	os.system("CLS")
	print(message)
	time.sleep(3)
	from main import menu
	menu()
