from datetime import datetime
import random

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
        self.level = None

    def get_first_name(self):
        """

        :return:
        """
        first_name = input("{} first name: ".format(ENTER))
        while Donor.is_valid_name(first_name) is False:
            first_name = input("{}\nThe first name can contain only letters and has to be at least 2 characters long!\
            \n{} first name: ".format(AGAIN, ENTER))
        self.first_name = first_name

    def get_last_name(self):
        """

        :return:
        """
        last_name = input("{} last name: ".format(ENTER))
        while Donor.is_valid_name(last_name) is False:
            last_name = input("{}\nThe last name can contain only letters and has to be at least 2 characters long!\
            \n{} last name: ".format(AGAIN, ENTER))
        self.last_name = last_name

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
        weight = input("{} weight: ".format(ENTER))
        while Donor.is_valid_weight(weight) is False:
            weight = input("{}\nThe weight has to be a positive number\n{} weight: ".format(AGAIN, ENTER))
        self.weight = weight

    def get_hemo_level(self):
        level = (random.randrange(80, 200))
        print(level)
        self.level = level

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
        gender = input("\nPlease enter an F for female or an M for male donor: ")
        while Donor.is_valid_gender(gender) is False:
            gender = input("{}\nYou can only choose the letter F or M! \
            \nPlease enter an F for female or an M for male donor: ".format(AGAIN))
        self.gender = gender

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
        date_of_birth = input("{} date of birth in the following format, 1999.12.31: ".format(ENTER))
        while Donor.is_valid_date(date_of_birth) is False:
            date_of_birth = input(
                "{}\n{} date of birth in the following format, 1999.12.31: ".format(AGAIN, ENTER))
        self.date_of_birth = date_of_birth

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
        donation_date = input("\nIf you have donated blood before, please enter its date \
                                    \nin the following format 1999.12.31, if not then press Enter: ")
        while Donor.is_valid_donation_date(donation_date) is False:
            donation_date = input("{}\nIf you have donated blood before, please enter its date \
                                    \nin the following format 1999.12.31, if not then press Enter: ".format(AGAIN))
        self.donation_date = donation_date

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
        sickness = input("\nWere you sick in the last month? For yes press Y for no press N: ")
        while Donor.is_valid_sickness(sickness) is False:
            sickness = input("{}\nWere you sick in the last month? Please press either Y or N: ".format(AGAIN))
        self.sickness = sickness

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
        id_number = input("\n{} unique identifier in the following format 123456AB or AB123456: ".format(ENTER))
        while Donor.is_valid_id_number(id_number) is False:
            id_number = input(
                "{}\n{} unique identifier in the following format 123456AB or AB123456: ".format(AGAIN, ENTER))
        self.id_number = id_number

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
        exp_date = input("{} ID expiration date in the following format 1999.12.31: ".format(ENTER))
        while Donor.is_valid_date(exp_date) is False:
            exp_date = input("{} {} ID expiration date in the following format 1999.12.31: ".format(AGAIN, ENTER))
        self.exp_date = exp_date

    def get_blood_type(self):
        """

        :return:
        """
        blood_type = input("{} type of blood from the following list: {}: ".format(ENTER, BLOOD))
        while Donor.is_valid_blood_type(blood_type) is False:
            blood_type = input("{}\n{} type of blood from the following list: {}: ".format(AGAIN, ENTER, BLOOD))
        self.blood_type = blood_type

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
        email_address = input("{} email address: ".format(ENTER))
        while Donor.is_valid_email_address(email_address) is False:
            email_address = input("{}\nThe email has to contain an @ and end with either .hu or .com.\
            \n{} email address: ".format(AGAIN, ENTER))
        self.email_address = email_address

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
        mobile_number = input("{} mobile number in the following format +36301234567: ".format(ENTER))
        while Donor.is_valid_mobile_number(mobile_number) is False:
            mobile_number = input("{}\n{} mobile number in the following format +36301234567: ".format(AGAIN, ENTER))
        self.mobile_number = mobile_number

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


