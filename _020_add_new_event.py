from _021_event_inputs import Event
from os import path
import csv
from datetime import datetime

user = Event()

event_id = str(datetime.now().strftime("%Y%m%d%H%M%S"))[2:]


def call_get_event_inputs():
	"""

	:return:
	"""
	user.get_date_of_event()
	while datetime.strptime(user.date_of_event, "%Y.%m.%d").isoweekday() == 6 or\
			datetime.strptime(user.date_of_event, "%Y.%m.%d").isoweekday() == 7 or\
			(datetime.strptime(user.date_of_event, "%Y.%m.%d") - datetime.now()).days < 10:
		print("Wrong input! The event can not be on weekends and has to be at least 10 days later than the current date.")
		user.get_date_of_event()
	user.get_start_time()
	user.get_end_time()
	while (int(str(user.start_time).replace(':', '')) + 100) > (int(str(user.end_time).replace(':', ''))):
		print("Wrong input! The end time has to be at least one hour later than the start time.")
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
		print("\nUnsuccessful, not worth to organise there again")
	if 0.2 <= float(user.successful_donations) / float(user.planned_donors) <= 0.75:
		print("\nNormal event")
	if 0.75 <= float(user.successful_donations) / float(user.planned_donors) <= 1.1:
		print("\nSuccessful")
	if float(user.successful_donations) / float(user.planned_donors) > 1.1:
		print("\nOutstanding")


def write_event_data_in_file():
	"""

	:return:
	"""
	event_data = [
		event_id,
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
