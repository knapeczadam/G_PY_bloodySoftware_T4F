from _021_event_inputs import Event
from datetime import datetime

user = Event()


def call_get_event_inputs():
	"""

	:return:
	"""
	user.generate_event_id()
	event_requirements(user.get_date_of_event())
	user.get_start_time()
	event_requirements(user.get_end_time())
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


def event_data_in_file():
	"""

	:return:
	"""
	event_data = [
		user.event_id,
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
	return event_data


def event_first_row():
	"""

	:return:
	"""
	first_row = [
		"Event ID",
		"Date of Event",
		"Start time",
		"End time",
		"Zip code",
		"City",
		"Address",
		"Available beds",
		"Planned donors",
		"Max donor numbers",
		"Successful donations"
	]
	return first_row


def event_requirements(get_something):
	"""

	:return:
	"""
	if user.date_of_event is not None and datetime.strptime(user.date_of_event, "%Y.%m.%d").isoweekday() == 6 or \
		datetime.strptime(user.date_of_event, "%Y.%m.%d").isoweekday() == 7 or \
					(datetime.strptime(user.date_of_event, "%Y.%m.%d") - datetime.now()).days < 10:
		print("Wrong input! The event can not be on weekends and has to be at least 10 days later than the current date.")
		event_requirements(user.get_date_of_event())
	if user.start_time is not None and user.end_time is not None and \
					(int(str(user.start_time).replace(':', '')) + 100) > (int(str(user.end_time).replace(':', ''))):
		print("Wrong input! The end time has to be at least one hour later than the start time.")
		event_requirements(user.get_end_time())