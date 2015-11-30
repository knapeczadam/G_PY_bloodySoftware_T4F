from datetime import timedelta
from datetime import datetime

PREPARATION_TIME = 30
DONATION_TIME = 30
AGAIN = "\nWrong input!"
ENTER = "\nPlease enter the"
CITIES = ("Miskolc", "Sarospatak", "Szerencs", "Kazincbarcika")


class Event:
	def __init__(self):
		self.date_of_event = None
		self.start_time = ""
		self.end_time = ""
		self.zip_code = None
		self.city = None
		self.address = None
		self.available_beds = None
		self.planned_donors = None
		self.max_donor_number = None
		self.successful_donations = None

	def get_date_of_event(self):
		"""

		:return:
		"""
		date_of_event = input("{} event date in the following format, 1999.12.31: ".format(ENTER))
		while Event.is_valid_date_of_event(date_of_event) is False:
			date_of_event = input("{}{} event date in the given format, 1999.12.31: ".format(AGAIN, ENTER))
		self.date_of_event = date_of_event

	@staticmethod
	def is_valid_date_of_event(event_date):
		"""

		:param event_date:
		:return:
		"""
		try:
			event_date = datetime.strptime(event_date, "%Y.%m.%d")
			if event_date.isoweekday() == 6 or event_date.isoweekday() == 7:
				return False
			if (event_date.date() - datetime.now().date()).days < 10:
				return False
			return True
		except:
			return False

	def get_start_time(self):
		"""

		:return:
		"""
		start_time = input("{} start time of the donation event in the following format, 09:30: ".format(ENTER))
		while Event.is_valid_start_time(start_time) is False:
			start_time = input("{}{} start time of the donation event in the following format, 09:30: ".format(AGAIN, ENTER))
		self.start_time = start_time

	@staticmethod
	def is_valid_start_time(start_time):
		"""

		:param start_time:
		:return:
		"""
		try:
			datetime.strptime(start_time, "%H:%M")
			return True
		except:
			return False

	def get_end_time(self):
		"""

		:return:
		"""
		end_time = input("{} end time of the donation event in the following format, 15:30:".format(ENTER))
		while self.is_valid_end_time(end_time) is False:
			end_time = input("{}\nThe end time has to be at least one hour later than the start time\
			\nand use the following format, 15:30: ".format(AGAIN, ENTER))
		self.end_time = end_time

	def is_valid_end_time(self, end_time):
		"""
		:param end_time:
		:return:
		"""
		if (int(str(self.start_time).replace(':', '')) + 100) > (int(str(end_time).replace(':', ''))):
			return False
		try:
			datetime.strptime(end_time, "%H:%M")
			return True
		except:
			return False

	def get_zip_code(self):
		"""

		:return:
		"""
		zip_code = input("{} zip: ".format(ENTER))
		while Event.is_valid_zip_code(zip_code) is False:
			zip_code = input("{} : ".format(AGAIN))
		self.zip_code = zip_code

	@staticmethod
	def is_valid_zip_code(zip_code):
		"""

		:param zip_code:
		:return:
		"""
		return zip_code.isdigit() and len(zip_code) == 4 and zip_code[0] != "0"

	def get_city(self):
		"""

		:return:
		"""
		city = input("Please type in where will the event take place; {}: ".format(CITIES))
		while Event.is_valid_city(city) is False:
			city = input("{} : ".format(AGAIN))
		self.city = city

	@staticmethod
	def is_valid_city(city):
		for cities in CITIES:
			if cities.lower() == city.lower():
				return True

	def get_address(self):
		"""

		:return:
		"""
		address = input("Please enter in what address will the event take place: ")
		while Event.is_valid_address(address) is False:
			address = input("{} : ".format(AGAIN))
		self.address = address

	@staticmethod
	def is_valid_address(address):
		"""

		:param address:
		:return:
		"""
		return 0 < len(address) <= 25

	def get_available_beds(self):
		"""

		:return:
		"""
		available_beds = input("Please enter the number of available beds: ")
		while Event.is_valid_available_beds(available_beds) is False:
			available_beds = input("{} : ".format(AGAIN))
		self.available_beds = available_beds

	@staticmethod
	def is_valid_available_beds(beds):
		"""

		:param beds:
		:return:
		"""
		return beds.isdigit() and int(beds) > 0

	def get_planned_donor_number(self):
		"""

		:return:
		"""
		planned_donors = input("Please enter the planned donor number: ")
		while self.is_valid_planned_donor_number(planned_donors) is False:
			planned_donors = input("{} : ".format(AGAIN))
		self.planned_donors = planned_donors

	def is_valid_planned_donor_number(self, planned_donors):
		"""

		:param planned_donors:
		:return:
		"""
		return planned_donors.isdigit() and int(planned_donors) <= self.max_donor_number

	def calc_max_donor_number(self):
		"""

		:return:
		"""
		event_duration_in_minutes = datetime.strptime(self.end_time, "%H:%M") - datetime.strptime(self.start_time, "%H:%M")
		event_duration_in_minutes = timedelta.total_seconds(event_duration_in_minutes) // 60
		max_donor_number = ((event_duration_in_minutes - PREPARATION_TIME) // DONATION_TIME) * int(self.available_beds)
		self.max_donor_number = max_donor_number

	def get_successful_donations(self):
		"""

		:return:
		"""
		successful_donations = input("Please enter how many successful donations\
	were during donation event (x out of {})".format(self.planned_donors))
		while Event.is_valid_successful_donations(successful_donations) is False:
			self.successful_donations = input("Please enter how many successful donations\
	were during donation event (x out of {})".format(self.planned_donors))
		self.successful_donations = successful_donations

	@staticmethod
	def is_valid_successful_donations(successful_donations):
		"""

		:param successful_donations:
		:return:
		"""
		return successful_donations.isdigit()
