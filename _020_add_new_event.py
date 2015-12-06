from _021_event_inputs import Event
from datetime import datetime

SATURDAY = 6
SUNDAY = 7
MIN_EVENT_TIME_IN_HOUR = 100  # 100 / 100 = 1h wrong variable expression
MIN_DAYS_BEF_NEW_EVENT = 10

UNSUC_EV_IN_PREX_MAX = 0.2  # 20%
NORM_EV_IN_PREC_MAX = 0.75  # 75 %
SUCC_EV_IN_PREC_MAX = 1.1  # 110 %

new_event = Event()


def call_event_get_functions():
	"""

	:return:
	"""
	new_event.generate_event_id()
	event_requirements(new_event.get_date_of_event())
	new_event.get_start_time()
	event_requirements(new_event.get_end_time())
	new_event.get_zip_code()
	new_event.get_city()
	new_event.get_address()
	new_event.get_available_beds()
	new_event.calc_max_donor_number()
	new_event.get_planned_donor_number()
	new_event.get_successful_donations()
	return True


def print_donation_successful():
	"""

	:return:
	"""

	if float(new_event.successful_donations) / float(new_event.planned_donors) < UNSUC_EV_IN_PREX_MAX:
		print("\nUnsuccessful, not worth to organise there again")
	if UNSUC_EV_IN_PREX_MAX <= float(new_event.successful_donations) / float(new_event.planned_donors) <= NORM_EV_IN_PREC_MAX:
		print("\nNormal event")
	if NORM_EV_IN_PREC_MAX <= float(new_event.successful_donations) / float(new_event.planned_donors) <= SUCC_EV_IN_PREC_MAX:
		print("\nSuccessful")
	if float(new_event.successful_donations) / float(new_event.planned_donors) > SUCC_EV_IN_PREC_MAX:
		print("\nOutstanding")


def new_event_to_list():
	"""

	:return:
	"""
	event_data = [
		new_event.event_id,
		new_event.date_of_event,
		new_event.start_time,
		new_event.end_time,
		new_event.zip_code,
		new_event.city,
		new_event.address,
		new_event.available_beds,
		new_event.planned_donors,
		new_event.max_donor_number,
		new_event.successful_donations
	]
	return event_data


def event_first_row():
	"""

	:return:
	"""
	event_header = [
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
	return event_header


def event_requirements(get_something):
	"""

	:return:
	"""
	if new_event.date_of_event is not None and datetime.strptime(new_event.date_of_event, "%Y.%m.%d").isoweekday() == SATURDAY or \
		datetime.strptime(new_event.date_of_event, "%Y.%m.%d").isoweekday() == SUNDAY or \
					(datetime.strptime(new_event.date_of_event, "%Y.%m.%d") - datetime.now()).days < MIN_DAYS_BEF_NEW_EVENT:
		print("Wrong input! The event can not be on weekends and has to be at least 10 days later than the current date.")
		event_requirements(new_event.get_date_of_event())
	if new_event.start_time is not None and new_event.end_time is not None and \
					(int(str(new_event.start_time).replace(':', '')) + MIN_EVENT_TIME_IN_HOUR) > (int(str(new_event.end_time).replace(':', ''))):
		print("Wrong input! The end time has to be at least one hour later than the start time.")
		event_requirements(new_event.get_end_time())