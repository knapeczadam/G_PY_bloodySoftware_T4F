from _021_event_inputs import Event
from os import path
import csv

user = Event()


def call_get_event_inputs():
	"""

	:return:
	"""
	user.get_date_of_event()
	user.get_start_time()
	user.get_end_time()
	user.get_zip_code()
	user.get_city()
	user.get_address()
	user.get_available_beds()
	user.calc_max_donor_number()
	user.get_planned_donor_number()
	user.get_successful_donations()


def print_donation_successful():
	"""

	:return:
	"""
	if float(user.successful_donations) / float(user.planned_donors) < 0.2:
		print("Unsuccessful, not worth to organise there again")
	if 0.2 <= float(user.successful_donations) / float(user.planned_donors) <= 0.75:
		print("Normal event")
	if 0.75 <= float(user.successful_donations) / float(user.planned_donors) <= 1.1:
		print("Successful")
	if float(user.successful_donations) / float(user.planned_donors) > 1.1:
		print("Outstanding")


def write_event_data_in_file():
	"""

	:return:
	"""
	event_data = [
		user.date_of_event,
		user.start_time,
		user.end_time,
		user.zip_code,
		user.city,
		user.address,
		user.available_beds,
		user.planned_donors,
		user.max_donor_number,
		user.successful_donations
	]

	if not (path.isfile("Data\events.csv")):
		f = open("Data\events.csv", 'w')
		f.close()

	with open("Data\events.csv", "a") as donors_csv:
		append_donor_data = csv.writer(donors_csv)
		append_donor_data.writerow(event_data)