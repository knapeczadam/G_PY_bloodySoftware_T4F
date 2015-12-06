from datetime import datetime
import random


GENDERS = ("F", "M")
ENTER = "\nPlease enter your"
AGAIN = "Wrong input!"
SICK = ["Y", "N"]
BLOOD = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', '0+', '0-']
PI = ("20", "30", "70")
ESC = "E"


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
		first_name = input("{} first name: ".format(ENTER))
		while Donor.is_valid_name(first_name) is not True:
			first_name = input("{}\nThe first name can contain only letters and has to be at least 2 characters long!\
			\n{} first name: ".format(AGAIN, ENTER))
		self.first_name = first_name

	def get_last_name(self):
		"""

		:return:
		"""
		last_name = input("{} last name: ".format(ENTER))
		while Donor.is_valid_name(last_name) is not True:
			last_name = input("{}\nThe last name can contain only letters and has to be at least 2 characters long!\
			\n{} last name: ".format(AGAIN, ENTER))
		self.last_name = last_name

	@staticmethod
	def is_valid_name(name: str):
		"""

		:param name:
		:return:
		"""
		return name.isalpha() and len(name) > 1 or name.upper() == ESC

	def get_weight(self):
		weight = input("{} weight: ".format(ENTER))
		while Donor.is_valid_weight(weight) is not True:
				weight = input("{}\nThe weight format is wrong!\
			\n{} weight: ".format(AGAIN, ENTER))
		self.weight = weight

	@staticmethod
	def is_valid_weight(weight: str):
		"""

		:param weight:
		:return:
		"""
		return weight.isdigit() and int(weight) > 0 or weight.upper() == ESC

	def get_gender(self):
		"""

		:return:
		"""
		gender = input("\nPlease enter an F for female or an M for male donor: ")
		while Donor.is_valid_gender(gender) is not True:
			gender = input("{}\nThe gender format is wrong!\
			\n{} gender: ".format(AGAIN, ENTER))
		self.gender = gender

	@staticmethod
	def is_valid_gender(gender: str):
		"""

		:param gender:
		:return:
		"""
		return gender.upper() in GENDERS or gender.upper() == ESC

	def get_date_of_birth(self):
		"""

		:return:
		"""
		date_of_birth = input("{} date of birth in the following format, 1999.12.31: ".format(ENTER))
		while Donor.is_valid_date(date_of_birth) is not True:
			date_of_birth = input("{}\nThe date of birth format is wrong!\
			\n{} date of birth: ".format(AGAIN, ENTER))
		self.date_of_birth = date_of_birth

	@staticmethod
	def is_valid_date(date: str):
		"""

		:param date:
		:return:
		"""
		try:
			if date.upper() == ESC:
				return True
			if datetime.strptime(date, "%Y.%m.%d") < datetime.now():
				return True
		except:
			return False

	def get_donation_date(self):
		"""

		:return:
		"""
		donation_date = input("\nIf you have donated blood before, please enter its date \
								\nin the following format 1999.12.31, if not then press Enter: ")
		while Donor.is_valid_donation_date(donation_date) is not True:
				donation_date = input("{}\nThe donation date format is wrong!\
			\n{} donation date: ".format(AGAIN, ENTER))
		self.donation_date = donation_date

	@staticmethod
	def is_valid_donation_date(date: str):
		"""

		:param date:
		:return:
		"""
		try:
			if date == "":
				return True
			if date.upper() == ESC:
				return True
			if datetime.strptime(date, "%Y.%m.%d") < datetime.now():
				return True
		except:
			return False

	def get_sickness(self):
		"""

		:return:
		"""
		sickness = input("\nWere you sick in the last month? For yes press Y for no press N: ")
		while Donor.is_valid_sickness(sickness) is not True:
				sickness = input("{}\nThe sickness format is wrong!\
			\n{} sickness: ".format(AGAIN, ENTER))
		self.sickness = sickness

	@staticmethod
	def is_valid_sickness(sickness: str):
		"""

		:param sickness:
		:return:
		"""
		return sickness.upper() in SICK or sickness.upper() == ESC

	def get_id_number(self):
		"""

		:return:
		"""
		id_number = input("{} unique identifier in the following format 123456AB or AB123456: ".format(ENTER))
		while Donor.is_valid_id_number(id_number) is not True:
				id_number = input("{}\nThe id number format is wrong!\
			\n{} id number: ".format(AGAIN, ENTER))
		self.id_number = id_number

	@staticmethod
	def is_valid_id_number(id_number: str):
		"""

		:param id_number:
		:return:
		"""
		if id_number.upper() == ESC:
			return True
		if not len(id_number) == 8:
			return False
		if not ((id_number[:6].isdigit() and id_number[6:].isupper()) or
					(id_number[:2].isupper() and id_number[2:].isdigit())):
			return False
		return True

	def get_exp_date(self):
		"""

		:return:
		"""
		exp_date = input("{} ID expiration date in the following format 1999.12.31: ".format(ENTER))
		while Donor.is_valid_exp_date(exp_date) is not True:
				exp_date = input("{}\nThe expiration date format is wrong!\
			\n{} expiration date : ".format(AGAIN, ENTER))
		self.exp_date = exp_date

	@staticmethod
	def is_valid_exp_date(date: str):
		"""

		:param date:
		:return:
		"""
		try:
			if date.upper() == ESC:
				return True
			if datetime.strptime(date, "%Y.%m.%d"):
				return True
		except:
			return False

	def get_blood_type(self):
		"""

		:return:
		"""
		blood_type = input("{} type of blood from the following list: {}: ".format(ENTER, BLOOD))
		while Donor.is_valid_blood_type(blood_type) is not True:
				blood_type = input("{}\nThe blood type is wrong!\
			\n{} blood type: ".format(AGAIN, ENTER))
		self.blood_type = blood_type

	@staticmethod
	def is_valid_blood_type(blood_type: str):
		"""

		:param blood_type:
		:return:
		"""
		return blood_type.upper() in BLOOD or blood_type.upper() == ESC

	def get_email_address(self):
		"""

		:return:
		"""
		email_address = input("{} email address: ".format(ENTER))
		while Donor.is_valid_email_address(email_address) is not True:
				email_address = input("{}\nThe email address format is wrong!\
			\n{} email address: ".format(AGAIN, ENTER))
		self.email_address = email_address

	@staticmethod
	def is_valid_email_address(email_address: str):
		"""

			:param email_address:
			:rtype: object
			:return:
			"""
		email_address = email_address.replace(" ", "")
		if email_address.upper() == ESC:
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
		mobile_number = input("{} mobile number in the following format +36301234567: ".format(ENTER))
		while Donor.is_valid_mobile_number(mobile_number) is not True:
				mobile_number = input("{}\nThe mobile number format is wrong!\
			\n{} mobile number: ".format(AGAIN, ENTER))
		self.mobile_number = mobile_number

	@staticmethod
	def is_valid_mobile_number(mobile_number: str):
		"""

		:param mobile_number:
		:return:
		"""
		mobile_number = mobile_number.replace(" ", "")
		if mobile_number.upper() == ESC:
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
