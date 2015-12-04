from datetime import datetime
import random
from msvcrt import getch

GENDERS = ("f", "m")
ENTER = "\nPlease enter your"
AGAIN = "Wrong input!"
SICK = ["y", "n"]
BLOOD = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', '0+', '0-']
PI = ("20", "30", "70")
ESC = ["exit"]


class Donor:
	def __init__(self):
		self.first_name = None
		self.last_name = None
		self.weight = None
		self.gender = None
		self.date_of_birth = None
		self.donation_date = None
		self.sickness = None
		self.id_number = None
		self.exp_date = None
		self.blood_type = None
		self.email_address = None
		self.mobile_number = None
		self.hemoglobin_level = None

	def get_first_name(self):
		"""

		:return:
		"""

		# first_name = input("{} first name: ".format(ENTER))

		print("Please enter your first name: ")
		first_name = getch()
		if first_name == b'\x1b':
			self.first_name = None

		if first_name != b'\x1b':
				y = str(first_name).replace("b'", "")
				y2 = y.replace("'", "")
				print(y2.upper(), end="")
				first_name2 = input()
				retu = y2 + str(first_name2)
				while Donor.is_valid_name(retu) is False:
					retu = input("{}\nThe first name can contain only letters and has to be at least 2 characters long!\
				\n{} first name: ".format(AGAIN, ENTER))
				self.first_name = retu

	def get_last_name(self):
		"""

		:return:
		"""
		# last_name = input("{} last name: ".format(ENTER))

		print("Please enter your last name: ")
		last_name = getch()
		if last_name == b'\x1b':
			self.last_name = None

		if last_name != b'\x1b':
				y = str(last_name).replace("b'", "")
				y2 = y.replace("'", "")
				print(y2.upper(), end="")
				last_name2 = input()
				retu = y2 + str(last_name2)
				while Donor.is_valid_name(retu) is False:
					retu = input("{}\nThe last name can contain only letters and has to be at least 2 characters long!\
				\n{} last name: ".format(AGAIN, ENTER))
				self.last_name = retu


	@staticmethod
	def is_valid_name(name):
		"""

		:param name:
		:return:
		"""
		return name.isalpha() and len(name) > 1

	def get_weight(self):
		"""

		:return:
		"""
		# weight = input("{} weight: ".format(ENTER))
		print("Please enter your Weight: ")
		weight = getch()
		if weight == b'\x1b':
			self.weight = None

		if weight != b'\x1b':
				y = str(weight).replace("b'", "")
				y2 = y.replace("'", "")
				print(y2.upper(), end="")
				weight2 = input()
				retu = y2 + str(weight2)
				while Donor.is_valid_weight(retu) is False:
					retu = input("{}\nThe weight format is wrong!\
				\n{} weight: ".format(AGAIN, ENTER))
				self.weight = int(retu)


	@staticmethod
	def is_valid_weight(weight):
		"""

		:param weight:
		:return:
		"""
		return weight.isdigit() and int(weight) > 0 or weight in ESC

	def get_gender(self):
		"""

		:return:
		"""
		# gender = input("\nPlease enter an F for female or an M for male donor: ")
		print("Please enter your Gender: ")
		gender = getch()
		if gender == b'\x1b':
			self.gender = None

		if gender != b'\x1b':
				y = str(gender).replace("b'", "")
				y2 = y.replace("'", "")
				print(y2.upper(), end="")
				gender2 = input()
				retu = y2 + str(gender2)
				while Donor.is_valid_gender(retu) is False:
					retu = input("{}\nThe gender format is wrong!\
				\n{} gender: ".format(AGAIN, ENTER))
				self.gender = retu

	@staticmethod
	def is_valid_gender(gender):
		"""

		:param gender:
		:return:
		"""
		return gender.lower() in GENDERS or gender in ESC

	def get_date_of_birth(self):
		"""

		:return:
		"""
		# date_of_birth = input("{} date of birth in the following format, 1999.12.31: ".format(ENTER))
		print("Please enter your Date of birth: ")
		date_of_birth = getch()
		if date_of_birth == b'\x1b':
			self.date_of_birth = None

		if date_of_birth != b'\x1b':
				y = str(date_of_birth).replace("b'", "")
				y2 = y.replace("'", "")
				print(y2.upper(), end="")
				date_of_birth2 = input()
				retu = y2 + str(date_of_birth2)
				while Donor.is_valid_date(retu) is False:
					retu = input("{}\nThe date_of_birth format is wrong!\
				\n{} date_of_birth: ".format(AGAIN, ENTER))
				self.date_of_birth = retu


	@staticmethod
	def is_valid_date(date):
		"""

		:param date:
		:return:
		"""
		try:
			if date in ESC:
				return True
			datetime.strptime(date, "%Y.%m.%d")
			return True
		except:
			return False

	def get_donation_date(self):
		"""

		:return:
		"""
		#donation_date = input("\nIf you have donated blood before, please enter its date \
									#\nin the following format 1999.12.31, if not then press Enter: ")
		print("\nIf you have donated blood before, please enter its date \
									\nin the following format 1999.12.31, if not then press Enter: ")
		donation_date = getch()
		if donation_date == b'\r':
			self.donation_date = ""
		elif donation_date == b'\x1b':
			self.donation_date = None

		elif donation_date != b'\x1b':
				y = str(donation_date).replace("b'", "")
				y2 = y.replace("'", "")
				print(y2.upper(), end="")
				donation_date2 = input()
				retu = y2 + str(donation_date2)
				while Donor.is_valid_donation_date(retu) is False:
					retu = input("{}\nThe donation_date format is wrong!\
				\n{} donation_date: ".format(AGAIN, ENTER))
				self.donation_date = retu


	@staticmethod
	def is_valid_donation_date(date):
		"""

		:param date:
		:return:
		"""
		try:
			if date == "":
				return True
			if date in ESC:
				return True
			datetime.strptime(date, "%Y.%m.%d")
			return True
		except:
			return False

	def get_sickness(self):
		"""

		:return:
		"""
		# sickness = input("\nWere you sick in the last month? For yes press Y for no press N: ")
		print("\nWere you sick in the last month? For yes press Y for no press N: ")
		sickness = getch()
		if sickness == b'\x1b':
			self.sickness = None

		if sickness != b'\x1b':
				y = str(sickness).replace("b'", "")
				y2 = y.replace("'", "")
				print(y2.upper(), end="")
				sickness2 = input()
				retu = y2 + str(sickness2)
				while Donor.is_valid_sickness(retu) is False:
					retu = input("{}\nThe sickness format is wrong!\
				\n{} sickness: ".format(AGAIN, ENTER))
				self.sickness = retu
	@staticmethod
	def is_valid_sickness(sickness):
		"""

		:param sickness:
		:return:
		"""
		return sickness.lower() in SICK or sickness in ESC

	def get_id_number(self):
		"""

		:return:
		"""
		#id_number = input("{} unique identifier in the following format 123456AB or AB123456: ".format(ENTER))
		print("{} unique identifier in the following format 123456AB or AB123456: ".format(ENTER))
		id_number = getch()
		if id_number == b'\x1b':
			self.id_number = None

		if id_number != b'\x1b':
				y = str(id_number).replace("b'", "")
				y2 = y.replace("'", "")
				print(y2.upper(), end="")
				id_number2 = input()
				retu = y2 + str(id_number2)
				while Donor.is_valid_id_number(retu) is False:
					retu = input("{}\nThe id_number format is wrong!\
				\n{} id_number: ".format(AGAIN, ENTER))
				self.id_number = retu

	@staticmethod
	def is_valid_id_number(id_number):
		"""

		:param id_number:
		:return:
		"""
		if id_number in ESC:
			return True
		if not len(id_number) == 8:
			return False
		if not ((id_number[:6].isdigit() and id_number[6:].isalpha()) or
					(id_number[:2].isalpha() and id_number[2:].isdigit())):
			return False
		return True

	def get_exp_date(self):
		"""

		:return:
		"""
		#exp_date = input("{} ID expiration date in the following format 1999.12.31: ".format(ENTER))
		print("{} ID expiration date in the following format 1999.12.31: ".format(ENTER))
		exp_date = getch()
		if exp_date == b'\x1b':
			self.exp_date = None

		if exp_date != b'\x1b':
				y = str(exp_date).replace("b'", "")
				y2 = y.replace("'", "")
				print(y2.upper(), end="")
				exp_date2 = input()
				retu = y2 + str(exp_date2)
				while Donor.is_valid_date(retu) is False:
					retu = input("{}\nThe exp_date format is wrong!\
				\n{} exp_date: ".format(AGAIN, ENTER))
				self.exp_date = retu

	def get_blood_type(self):
		"""

		:return:
		"""
		#blood_type = input("{} type of blood from the following list: {}: ".format(ENTER, BLOOD))
		print("{} type of blood from the following list: {}: ".format(ENTER, BLOOD))
		blood_type = getch()
		if blood_type == b'\x1b':
			self.blood_type = None

		if blood_type != b'\x1b':
				y = str(blood_type).replace("b'", "")
				y2 = y.replace("'", "")
				print(y2.upper(), end="")
				blood_type2 = input()
				retu = y2 + str(blood_type2)
				while Donor.is_valid_blood_type(retu) is False:
					retu = input("{}\nThe blood_type format is wrong!\
				\n{} blood_type: ".format(AGAIN, ENTER))
				self.blood_type = retu

	@staticmethod
	def is_valid_blood_type(blood_type):
		"""

		:param blood_type:
		:return:
		"""
		return blood_type.upper() in BLOOD or blood_type in ESC

	def get_email_address(self):
		"""

		:return:
		"""
		#email_address = input("{} email address: ".format(ENTER))
		print("{} email address: ".format(ENTER))
		email_address = getch()
		if email_address == b'\x1b':
			self.email_address = None

		if email_address != b'\x1b':
				y = str(email_address).replace("b'", "")
				y2 = y.replace("'", "")
				print(y2, end="")
				email_address2 = input()
				retu = y2 + str(email_address2)
				while Donor.is_valid_email_address(retu) is False:
					retu = input("{}\nThe email_address format is wrong!\
				\n{} email_address: ".format(AGAIN, ENTER))
				self.email_address = retu

	@staticmethod
	def is_valid_email_address(email_address):
		"""

			:param email_address:
			:rtype: object
			:return:
			"""
		email_address = email_address.replace(" ", "")
		if email_address in ESC:
			return True
		if not (len(email_address) > 5 or len(email_address) > 6):
			return False
		if "@" not in email_address and email_address.index("@") > 0:
			return False
		if not (email_address.endswith((".hu", ".com"))):
			return False
		at_sign_index = email_address.index('@')
		if not (email_address[at_sign_index + 1:len(email_address) - 4].isalpha() or
					email_address[at_sign_index + 1:len(email_address) - 3].isalpha()):
			return False
		if not (email_address[0].isalpha() and email_address[at_sign_index - 1].isalpha()):
			return False
		at_sign_number = 0
		for letter in email_address:
			if letter == "@":
				at_sign_number += 1
				if at_sign_number > 1:
					return False
		return True

	def get_mobile_number(self):
		"""

		:return:
		"""
		#mobile_number = input("{} mobile number in the following format +36301234567: ".format(ENTER))
		print("{} mobile number in the following format +36301234567: ".format(ENTER))
		mobile_number = getch()
		if mobile_number == b'\x1b':
			self.mobile_number = None

		if mobile_number != b'\x1b':
				y = str(mobile_number).replace("b'", "")
				y2 = y.replace("'", "")
				print(y2.upper(), end="")
				mobile_number2 = input()
				retu = y2 + str(mobile_number2)
				while Donor.is_valid_mobile_number(retu) is False:
					retu = input("{}\nThe mobile_number format is wrong!\
				\n{} mobile_number: ".format(AGAIN, ENTER))
				self.mobile_number = retu

	@staticmethod
	def is_valid_mobile_number(mobile_number):
		"""

		:param mobile_number:
		:return:
		"""
		mobile_number = mobile_number.replace(" ", "")
		if mobile_number in ESC:
			return True
		if not (mobile_number[:12].isdigit() or mobile_number[1:13].isdigit()):
			return False
		if not mobile_number.startswith(('06', '+36')):
			return False
		if not ((mobile_number[3:5] in PI) or (mobile_number[2:4] in PI)):
			return False
		if not (mobile_number[2:4] in PI and len(mobile_number) == 11 or
							mobile_number[3:5] in PI and len(mobile_number) == 12):
			return False
		return True

	def get_hemo_level(self):
		"""

		:return:
		"""
		hemoglobin_level = (random.randrange(80, 201))
		self.hemoglobin_level = hemoglobin_level
