from datetime import datetime


# VALIDATOR CLASS
class DonorValidator:

    # NAME
    # TDD VAN
    def is_valid_name(self):
        split_name = str(self).split(" ")
        return str(self).replace(" ", "").isalpha() and len(split_name) > 1

    # GENDER
    # TDD VAN
    def is_valid_gender(self):
        available_genders = ["f", "m"]
        return str(self).lower() in available_genders

    # WEIGHT
    # TDD VAN
    def is_valid_weight(self):
        return str(self).isdigit()

    # DATE
    # TDD VAN
    def is_valid_date(self):
        try:
            datetime.strptime(str(self), "%Y.%m.%d")
            return True
        except:
            return False

    # SICKNESS
    # TDD VAN
    def is_valid_sickness(self):
        yes_or_no = ["y", "n"]
        return str(self).lower() in yes_or_no

    # ID NUMBER
    # TDD VAN
    def is_valid_id_number(self):

        if len(str(self)) != 8 or not str(self).isalnum():
            return False
        if str(self)[:6].isdigit() and str(self)[6:].isalpha():
            print("The donor's ID number has been recorded.")
            return True
        elif str(self)[:2].isalpha() and str(self)[2:].isdigit():
            print("The donor's passport number has been recorded.")
            return True
        else:
            print("Not ID or passport, but the given input has been recorded.")
            return True

    # BLOOD TYPE
    # TDD VAN
    def is_valid_blood_type(self):
        blood_types = ["a", "b", "ab", "0"]
        return str(self).lower() in blood_types

    # EMAIL ADDRESS
    # TDD VAN
    def is_valid_email_address(self):
        email_address_string = str(self).replace(" ", "")

        contains_at_sign = "@" in email_address_string and email_address_string.index("@") > 0
        ending_is_valid = email_address_string.endswith(".hu") or email_address_string.endswith(".com")

        if not contains_at_sign:
            print("Please add an '@' sign to your address!")
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


# INPUT HELPER CLASS
class DonorInputHelper:

    @staticmethod
    def Input():
        global Input
        Input = input("--->")
        return Input

    # NAME
    @staticmethod
    def get_name():
        print("Enter the donor's name (eg.: John Doe):")
        while DonorValidator.is_valid_name(DonorInputHelper.Input()) is False:
            print("Please reenter the name in a valid format (eg.: John Doe):")
        return Input

    # GENDER
    @staticmethod
    def get_gender():
        print("Enter the donor's gender (F/M):")
        while DonorValidator.is_valid_gender(DonorInputHelper.Input()) is False:
            print("Please enter the donor's gender in a valid format (F/M):")
        return Input

    # WEIGHT
    @staticmethod
    def get_weight():
        print("Enter the donor's weight:")
        while DonorValidator.is_valid_weight(DonorInputHelper.Input()) is False:
            print("Please enter only numbers:")
        return Input

    # DATE OF BIRTH
    @staticmethod
    def get_date_of_birth():
        print("Enter the donor's date of birth in the following format, YYYY.MM.DD:")
        while DonorValidator.is_valid_date(DonorInputHelper.Input()) is False:
            print("Please enter the date in a valid format (YYYY.MM.DD):")
        return Input

    # DONATION DATE
    @staticmethod
    def get_donation_date():
        print("Enter the donor's last donation date in the following format, YYYY.MM.DD: ")
        while DonorValidator.is_valid_date(DonorInputHelper.Input()) is False:
            print("Please enter the date in a valid format (YYYY.MM.DD):")
        return Input

    # SICKNESS
    @staticmethod
    def get_sickness():
        print("Was the donor sick in last month? Y/N")
        while DonorValidator.is_valid_sickness(DonorInputHelper.Input()) is False:
            print("Please enter a valid input (Y or N only):")
        return Input

    # ID NUMBER
    @staticmethod
    def get_id_number():
        print("Enter the donor's ID or passport number (eight characters):")
        while DonorValidator.is_valid_id_number(DonorInputHelper.Input()) is False:
            print("Please reenter the ID or passport number in a valid form (eight characters):")
        return Input

    # ID EXPIRATION DATE
    @staticmethod
    def get_exp_date():
        print("Enter the donor's ID expiration date")
        while DonorValidator.is_valid_date(DonorInputHelper.Input()) is False:
            print("Please enter the date in a valid format (YYYY.MM.DD):")
        return Input

    # BLOOD TYPE
    @staticmethod
    def get_blood_type():
        print("Enter the donor's blood type (the valid inputs are a, b, ab, 0):")
        while DonorValidator.is_valid_blood_type(DonorInputHelper.Input()) is False:
            print("Please enter the blood type in a valid format (a, b, ab, 0):")
        return Input

    # EMAIL ADDRESS
    @staticmethod
    def get_email_address():
        print("Enter the donor's email address (only .hu or .com)")
        while DonorValidator.is_valid_email_address(DonorInputHelper.Input()) is False:
            print("Please enter the email address in a valid form (eg.: johndoe@gmail.com)")
        return Input

    # MOBILE NUMBER
    @staticmethod
    def get_mobile_number():
        print("Enter the donor's mobile number (valid country '+36/06', valid providers '20/30/70'):")
        while DonorValidator.is_valid_mobile_number(DonorInputHelper.Input()) is False:
            print("Please enter the mobile number in a valid form (eg.: 06301234567):")
        return Input
