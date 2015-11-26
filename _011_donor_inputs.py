from datetime import datetime

GENDERS = ("f", "m")
ENTER = "Please enter your"
AGAIN = "Wrong input!"
SICK = ["y", "n"]
BLOOD = ["a+", "a-", "b+", "b-", "ab+", "ab-", "0+", "0-"]
PI = ("20", "30", "70")


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

	def get_first_name(self):
		"""

		:return:
		"""
		self.first_name = input("{} first name: ".format(ENTER))
		while Donor.is_valid_name(self.first_name) is False:
			self.first_name = input("{}\nThe first name can contain only letters and has to be at least 2 \
			characters long!\n{} first name: ".format(AGAIN, ENTER))
		return self.first_name

	def get_last_name(self):
		"""

		:return:
		"""
		self.last_name = input("{} last name: ".format(ENTER))
		while Donor.is_valid_name(self.last_name) is False:
			self.last_name = input("{}\nThe last name can contain only letters and has to be at least 2 \
			characters long!\n{} last name: ".format(AGAIN, ENTER))
		return self.last_name

	def is_valid_name(name):
		"""

		:return:
		"""
		return name.isalpha() and len(name) > 1

	def get_weight(self):
		"""

		:return:
		"""
		self.weight = input("{} weight: ".format(ENTER))
		while Donor.is_valid_weight(self.weight) is False:
			self.weight = input("{}\nThe weight has to be a positive number\n{} weight: ".format(AGAIN, ENTER))
		return self.weight

	def is_valid_weight(weight):
		"""

		:return:
		"""
		return weight.isdigit() and int(weight) > 0

	def get_gender(self):
		"""

		:return:
		"""
		self.gender = input("Please enter an F if you are a Female or an M if you are a Male: ")
		while Donor.is_valid_gender(self.gender) is False:
			self.gender = input("{}\nYou can only choose the letter F or M! \
			\nPlease enter an F if you are a Female or an M if you are a Male: ".format(AGAIN))
		return self.gender

	def is_valid_gender(gender):
		"""

		:return:
		"""
		return gender.lower() in GENDERS

	def get_date_of_birth(self):
		"""

		:return:
		"""
		self.date_of_birth = input("{} date of birth in the following format, 2000.12.31: ".format(ENTER))
		while Donor.is_valid_date(self.date_of_birth) is False:
			self.date_of_birth = input(
				"{}\n{} date of birth in the following format, 2000.12.31: ".format(AGAIN, ENTER))
		return self.date_of_birth

	def is_valid_date(date):
		"""

		:return:
		"""
		try:
			datetime.strptime(date, "%Y.%m.%d")
			return True
		except:
			return False

	def get_donation_date(self):
		"""

		:return:
		"""
		self.donation_date = input("If you have donated blood before, please enter its date \
		in the following format 2000.12.31 otherwise press ENTER: ")
		while Donor.is_valid_date(self.donation_date) is False:
			self.donation_date = input("{}\nIf you have donated blood before, please enter its date \
		in the following format 2000.12.31 otherwise press Enter: ".format(AGAIN))
		return self.donation_date

	def is_valid_donation_date(date):
		"""

		:return:
		"""
		try:
			if date == "":
				return True
			datetime.strptime(date, "%Y.%m.%d")
			return True
		except:
			return False

	def get_sickness(self):
		"""

		:return:
		"""
		self.sickness = input("Were you sick in the last month? For yes press Y for no press N: ")
		while Donor.is_valid_sickness(self.sickness) is False:
			self.sickness = input("{} Press either Y or N: ".format(AGAIN))
		return self.sickness

	def is_valid_sickness(sickness):
		"""

		:return:
		"""
		return sickness.lower() in SICK

	def get_id_number(self):
		"""

		:return:
		"""
		self.id_number = input("{} ID : ".format(ENTER))
		while Donor.is_valid_date(self.id_number) is False:
			self.id_number = input("{}  ".format(AGAIN, ENTER))
		return self.id_number

	def is_valid_id_number(id_number):
		"""

		:return:
		"""
		if not len(id_number) == 8:
			return False
		if not ((id_number[:6].isdigit() and id_number[6:9].isalpha()) or \
				(id_number[:2].isalpha() and id_number[2:9].isdigit())):
			return False
		return True

	def get_exp_date(self):
		"""

		:return:
		"""
		self.exp_date = input("{} ID expiration date in the following format 2000.12.31: ".format(ENTER))
		while Donor.is_valid_date(self.exp_date) is False:
			self.exp_date = input("{} {} ID expiration date in the following format 2000.12.31: ".format(AGAIN, ENTER))
		return self.exp_date

	def get_blood_type(self):
		"""

		:return:
		"""
		self.blood_type = input("{} type of blood: ".format(ENTER))
		while Donor.is_valid_blood_type(self.blood_type) is False:
			self.blood_type = input("{} {} type of blood: ".format(AGAIN, ENTER))
		return self.blood_type

	def is_valid_blood_type(blood_type):
		"""

		:return:
		"""
		return blood_type.lower() in BLOOD

	def get_email_address(self):
		"""

		:return:
		"""
		self.email_address = input("{} email: ".format(ENTER))
		while Donor.is_valid_email_address is False:
			self.email_address = input("{} ".format(AGAIN))
		return self.email_address

	def is_valid_email_address(email_address):
		"""

			:rtype: object
			:return:
			"""
		email_address = email_address.replace(" ", "")
		if not (len(email_address) > 5 or len(email_address) > 6):
			return False
		if "@" not in email_address and email_address.index("@") > 0:
			return False
		if not (email_address.endswith((".hu", ".com"))):
			return False
		at_sign_index = email_address.index('@')
		if not (email_address[at_sign_index + 1:len(email_address) - 4].isalpha() or\
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
		self.mobile_number = input("{} mobile number: ".format(ENTER))
		while Donor.is_valid_mobile_number(self.mobile_number) is False:
			self.mobile_number = input("{} ".format(AGAIN))
		return self.mobile_number

	def is_valid_mobile_number(mobile_number):
		"""

		:return:
		"""
		mobile_number = mobile_number.replace(" ", "")
		if not (mobile_number[:12].isdigit() or mobile_number[1:13].isdigit()):
			print()
			return False
		if not mobile_number.startswith(('06', '+36')):
			return False
		if not ((mobile_number[3:5] in PI) or (mobile_number[2:4] in PI)):
			return False
		if not (mobile_number[2:4] in PI and len(mobile_number) == 11 or \
								mobile_number[3:5] in PI and len(mobile_number) == 12):
			return False
		return True