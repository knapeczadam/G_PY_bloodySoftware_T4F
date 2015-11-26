from datetime import timedelta
from datetime import datetime

PREPARATION_TIME = 30
DONATION_TIME = 30
ENTER = "Please enter your"
AGAIN = "Wrong input!"
CITIES = ("Miskolc", "Sarospatak", "Szerencs", "Kazincbarcika")


class Event:
	def __init__(self):
		self.date_of_event = None
		self.start_time = None
		self.end_time = None
		self.zip_code = None
		self.city = None
		self.address = None
		self.available_beds = None
		self.planned_donors = None
		self.successful_donations = None

	def get_date_of_event(self):
		"""

		:return:
		"""
		self.date_of_event = input("{} event date: ".format(ENTER))
		while Event.is_valid_date(self.date_of_event) is False:
			self.date_of_event = input("{} : ".format(AGAIN))
		return self.date_of_event

	def is_valid_date_of_event(event_date):
		"""

		:return:
		"""
		try:
			if event_date == "":
				return True
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
		self.start_time = input("Enter the start of the donation: ")
		while Event.is_valid_time(self.start_time) is False:
			self.start_time = input("{} : ".format(AGAIN))
		return self.start_time

	def is_valid_start_time(start_time):
		"""

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
		self.end_time = input("Enter your donation end:")
		while Event.is_valid_time(self.end_time) is False:
			self.end_time = input("{} : ".format(AGAIN))
		return self.end_time

	def is_valid_end_time(self):
		"""

		:return:
		"""
		try:
			datetime.strptime(self, "%H:%M")
			if self.start_time > self.end_time:
				return False
			return True
		except:
			return False

	def get_zip_code(self):
		"""

		:return:
		"""
		self.zip_code = input("{} zip: ".format(ENTER))
		while Event.is_valid_zip_code(self.zip_code) is False:
			self.zip_code = input("{} : ".format(AGAIN))
		return self.zip_code

	def is_valid_zip_code(zip):
		"""

		:return:
		"""
		return zip.isdigit() and len(zip) == 4 and zip[0] != "0"

	def get_city(self):
		"""

		:return:
		"""
		self.city = input("Please type in where will the event take place; {}: ".format(CITIES))
		while Event.is_valid_city(self.city) is False:
			self.city = input("{} : ".format(AGAIN))
		return self.city

	def is_valid_city(city):
		for cities in CITIES:
			if cities.lower() == city.lower():
				return True

	def get_address(self):
		"""

		:return:
		"""
		self.address = input("Please enter in what address will the event take place: ")
		while Event.is_valid_address(self.address) is False:
			self.address = input("{} : ".format(AGAIN))
		return "'" + self.address + "'"

	def is_valid_address(address):
		"""

		:return:
		"""
		return 0 < len(address) <= 25

	def get_available_beds(self):
		"""

		:return:
		"""
		self.available_beds = input("Please enter the number of available beds: ")
		while Event.is_valid_available_beds(self.available_beds) is False:
			self.available_beds = input("{} : ".format(AGAIN))
		return self.available_beds

	def is_valid_available_beds(beds):
		"""

		:return:
		"""
		return beds.isdigit()

	def get_planned_donor_number(self):
		"""

		:return:
		"""
		self.planned_donors = input("Please enter the planned donor number: ")
		while Event.is_valid_planned_donor_number(self.planned_donors) is False:
			self.planned_donors = input("{} : ".format(AGAIN))
		return self.planned_donors

	def is_valid_planned_donor_number(planned_donors):
		"""

		:return:
		"""
		return planned_donors.isdigit() and int(planned_donors) <= max_donor_number

	def get_successful_donations(self):
		"""

		:return:
		"""
		self.successful_donations = input("Please enter how many successfull donations\
	were during donation event (x out of {})".format(max_donor_number))
		while Event.is_valid_successful_donations(self.successful_donations) is False:
			self.successful_donations = input("Please enter how many successfull donations\
	were during donation event (x out of {})".format(max_donor_number))
		return self.successful_donations

	def is_valid_successful_donations(successful_donations):
		"""

		:return:
		"""
		return successful_donations.isdigit()

	def calc_max_donor_number(self):
		"""

		:return:
		"""
		global max_donor_number
		event_duration_in_minutes = datetime.strptime(self.end_time, "%H:%M") \
									- datetime.strptime(self.start_time, "%H:%M")
		event_duration_in_minutes = timedelta.total_seconds(event_duration_in_minutes) // 60
		max_donor_number = ((event_duration_in_minutes - PREPARATION_TIME) \
							// DONATION_TIME) * int(self.available_beds)
		return max_donor_number