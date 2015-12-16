from csv_helper import pure_data_from_csv_file
from _011_donor_inputs import Donor
from datetime import datetime
import time
from mysql.connector import MySQLConnection, Error
from setup_database import connect_to_server

DONOR_PATH = "Data\donors.csv"
NOT_SUITABLE = "\nThe program has ended because of not suitable donor."

MIN_HEMO_LEVEL = 110
MIN_WEIGHT_IN_KG = 50
MIN_AGE_IN_YEAR = 18
MIN_NUMB_OF_DAYS_FROM_LAST_DONATION = 90
ONE_YEAR_IN_DAYS = 365

ESC = "E"
WAIT_IN_SEC = 1

new_donor = Donor()


def call_donor_get_functions():
	"""

	:return:
	"""
	donor_is_suitable = True
	pressed_e_key = False
	write_data_to_csv = None

	while donor_is_suitable and not pressed_e_key:
		new_donor.get_hemo_level()                                    # 1 - HEMOGLOBIN LEVEL
		if donor_isnt_suitable():
			break
		new_donor.get_weight()                                        # 2 - WEIGHT
		if donor_pressed_e_key(new_donor.weight):
			break
		if donor_isnt_suitable():
			break
		new_donor.get_date_of_birth()                                 # 3 - DATE OF BIRTH
		if donor_pressed_e_key(new_donor.date_of_birth):
			break
		if donor_isnt_suitable():
			break
		new_donor.get_donation_date()                                  # 4 - DONATION DATE
		if donor_pressed_e_key(new_donor.donation_date):
			break
		if donor_isnt_suitable():
			break
		new_donor.get_sickness()                                       # 5 - SICKNESS
		if donor_pressed_e_key(new_donor.sickness):
			break
		if donor_isnt_suitable():
			break
		new_donor.get_exp_date()                                       # 6 - EXPIRATION DATE
		if donor_pressed_e_key(new_donor.exp_date):
			break                                                      # -------------------------
		if donor_isnt_suitable():
			break
		new_donor.get_first_name()                                     # 7 - FIRST NAME
		if donor_pressed_e_key(new_donor.first_name):
			break
		new_donor.get_last_name()                                      # 8 - LAST NAME
		if donor_pressed_e_key(new_donor.last_name):
			break
		new_donor.get_id_number()                                      # 9 - ID
		while id_is_exist(new_donor.id_number):
			new_donor.get_id_number()
		if donor_pressed_e_key(new_donor.id_number):
			break
		new_donor.get_gender()                                         # 10 - GENDER
		if donor_pressed_e_key(new_donor.gender):
			break
		new_donor.get_blood_type()                                     # 11 - BLOOD TYPE
		if donor_pressed_e_key(new_donor.blood_type):
			break
		new_donor.get_email_address()                                  # 12 - EMAIL ADDRESS
		if donor_pressed_e_key(new_donor.email_address):
			break
		new_donor.get_mobile_number()                                  # 13 - MOBILE NUMBER
		if donor_pressed_e_key(new_donor.mobile_number):
			break
		if donor_is_suitable and not pressed_e_key:
			write_data_to_csv = True
			break
	return write_data_to_csv


def donor_isnt_suitable():
	"""

	:param :
	:return:
	"""
	if new_donor.hemoglobin_level is not None:                                                # 1 - HEMOGLOBIN LEVEL
		if new_donor.hemoglobin_level < MIN_HEMO_LEVEL:
			print("Your hemoglobin level is not high enough. Born again!")
			time.sleep(WAIT_IN_SEC)
			new_donor.hemoglobin_level = None
			return True
	if new_donor.weight is not None and new_donor.weight.upper() != ESC:                      # 2 - WEIGHT
		if int(new_donor.weight) <= MIN_WEIGHT_IN_KG:
			print("new_donors are only accepted above 50 kgs." + NOT_SUITABLE)
			time.sleep(WAIT_IN_SEC)
			new_donor.weight = None
			return True
	if new_donor.date_of_birth is not None and new_donor.date_of_birth.upper() != ESC:        # 3 - DATE OF BIRTH
		if calc_donor_input_to_days(new_donor.date_of_birth) // ONE_YEAR_IN_DAYS < MIN_AGE_IN_YEAR:
			print("new_donors are only accepted above 18 years." + NOT_SUITABLE)
			time.sleep(WAIT_IN_SEC)
			new_donor.date_of_birth = None
			return True
	if new_donor.donation_date is not None and new_donor.donation_date.upper() != ESC:         # 4 - DONATION DATE
		if new_donor.donation_date != "":
			if calc_donor_input_to_days(new_donor.donation_date) <= MIN_NUMB_OF_DAYS_FROM_LAST_DONATION:
				print("Donors can only give blood once in every 3 months." + NOT_SUITABLE)
				time.sleep(WAIT_IN_SEC)
				new_donor.donation_date = None
				return True
	if new_donor.sickness is not None:                                                         # 5 - SICKNESS
		if new_donor.sickness.lower() == "y":
			print(NOT_SUITABLE)
			time.sleep(WAIT_IN_SEC)
			new_donor.sickness = None
			return True
	if new_donor.exp_date is not None and new_donor.exp_date.upper() != ESC:                    # 6 - EXPIRATION DATE
		if datetime.strptime(new_donor.exp_date, "%Y.%m.%d") < datetime.now():
			print("The donor's ID is expired! Program is shutting down...")
			time.sleep(WAIT_IN_SEC)
			new_donor.exp_date = None
			return True


def donor_pressed_e_key(donor_input: str):
	if donor_input.upper() == ESC:
		return True


def id_is_exist(id_input):
	"""

	:param get_id_number:
	:return:
	"""
	id_index_in_row = 7
	pure_data = pure_data_from_csv_file(DONOR_PATH)
	for row in pure_data:
		if row[id_index_in_row] == id_input:
			print("ID is already exist!")
			return True


def donor_first_row():
	"""

	:return: list
	"""
	donor_header = [
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
		"Mobile number",
		"Hemoglobin level"
	]
	return donor_header


def new_donor_to_list():
	"""

	:return: list
	"""
	new_donor_data = [
		new_donor.first_name,
		new_donor.last_name,
		new_donor.weight,
		new_donor.gender,
		new_donor.date_of_birth,
		new_donor.donation_date,
		new_donor.sickness,
		new_donor.id_number,
		new_donor.exp_date,
		new_donor.blood_type,
		new_donor.email_address,
		new_donor.mobile_number,
		new_donor.hemoglobin_level
	]
	return new_donor_data


def print_suitable_donor_data():
	"""

	:return:
	"""
	donor_age_in_year = calc_donor_input_to_days(new_donor.date_of_birth) // ONE_YEAR_IN_DAYS
	donor_first_name_index_in_row = 0
	donor_last_name_index_in_row = 1
	donor_weight_index_in_row = 2
	donor_age_index_in_row = 4
	donor_email_index_in_row = 10
	print("\nNew donor has been added: \n{}, {} \n{} kg \n{}, {} years old \n{}".format
		  (new_donor_to_list()[donor_first_name_index_in_row],
		   new_donor_to_list()[donor_last_name_index_in_row],
		   new_donor_to_list()[donor_weight_index_in_row],
		   new_donor_to_list()[donor_age_index_in_row], donor_age_in_year,
		   new_donor_to_list()[donor_email_index_in_row]))
	if input("\nTo exit the program press E, to return to the Main menu press Enter: ").upper() == "E":
		exit()


def calc_donor_input_to_days(donor_input):
	if donor_input is not None:
		return (datetime.now() - datetime.strptime((donor_input), "%Y.%m.%d")).days


def insert_donor_data_into_table():
	database_connector, cursor = connect_to_server()
	cursor.execute("USE BloodDonationStorage")
	if new_donor.donation_date == "":
		new_donor.donation_date = '0000-00-00'
	insert = """INSERT INTO Donors(First_name,Last_name, Weight, Gender, Date_of_birth, Donation_date, Sickness, ID_number,
			Expiration_date, Blood_type, Email_address, Mobile_number, Hemoglobin_level)
			VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
		new_donor.first_name,
		new_donor.last_name,
		new_donor.weight,
		new_donor.gender,
		new_donor.date_of_birth,
		new_donor.donation_date,
		new_donor.sickness,
		new_donor.id_number,
		new_donor.exp_date,
		new_donor.blood_type,
		new_donor.email_address,
		new_donor.mobile_number,
		new_donor.hemoglobin_level
	)
	cursor.execute(insert)
	database_connector.commit()
	new_donor.donation_date = None

