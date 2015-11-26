from datetime import datetime

GENDERS = ("f", "m")
ENTER = "Please enter your"
AGAIN = "Wrong input!"
SICK = ["y", "n"]


class Donor:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.gender = None
        self.weight = None
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
        return str(weight).isdigit() and int(weight) > 0

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

    def get_exp_date(self):
        print("Please enter your ID experiment date:")
        while Donor.is_valid_date() is False:
            print("Try again!:")
        return Input

    def is_valid_id_number(self):

        if len(str(self)) != 8 or not str(self).isalnum():
            return False
        if str(self)[:6].isdigit() and str(self)[6:].isalpha():
            print("Your ID number is recorded.")
            return True
        elif str(self)[:2].isalpha() and str(self)[2:].isdigit():
            print("Your passport number is recorded.")
            return True
        else:
            print("Not ID or Pass, But recorded.")
            return True

    # BLOOD TYPE
    # TDD VAN
    def is_valid_blood_type(self):
        Blood_types = ["a", "b", "ab", "0"]
        return str(self).lower() in Blood_types

    # EMAIL ADDRESS
    # TDD VAN
    def is_valid_email_address(self):
        email_address_string = str(self).replace(" ", "")

        contains_at_sign = "@" in email_address_string and email_address_string.index("@") > 0
        ending_is_valid = email_address_string.endswith(".hu") or email_address_string.endswith(".com")

        if not contains_at_sign:
            print("Please add an '@' sign in your address!")
            return False
        if not ending_is_valid:
            print("Please specify where your email provider is ('.com' or '.hu')!")
            return False
        return True

    # MOBILE NUMBER
    # TDD VAN
    def is_valid_mobile_number(self):
        mobile_string = str(self).replace(" ", "")

        start_36_or_06 = mobile_string.startswith("+36") or mobile_string.startswith("06")

        contains_20_30_70 = "20" in mobile_string or "30" in mobile_string \
                            or "70" in mobile_string
        valid_length = len(mobile_string) == 11

        if not start_36_or_06:
            print("Please specify your number and add '36' or '06' at the beginning!")
            return False
        if not contains_20_30_70:
            print("Please specify your provider: 20/30/70 !")
            return False
        if not valid_length:
            print("Please enter a mobile number with a valid (11 number) length!")
            return False
        return True


    # ID NUMBER
    def get_id_number():
        print("Please enter your ID:")
        while DonorValidator.is_valid_id_number(DonorInputHelper.Input()) is False:
            print("Try again!:")
        return Input

    # ID EXPIRATION DATE


    # BLOOD TYPE
    def get_blood_type():
        print("Please enter your type of blood:")
        while DonorValidator.is_valid_blood_type(DonorInputHelper.Input()) is False:
            print("Try again!:")
        return Input

    # EMAIL ADDRESS
    def get_email_address():
        print("Please enter your email:")
        while DonorValidator.is_valid_email_address(DonorInputHelper.Input()) is False:
            print("Try again!:")
        return Input

    # MOBILE NUMBER
    def get_mobile_number():
        print("Please enter your mobile number:")
        while DonorValidator.is_valid_mobile_number(DonorInputHelper.Input()) is False:
            print("Try again!:")
        return Input
