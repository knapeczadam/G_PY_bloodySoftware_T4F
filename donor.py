from datetime import datetime


# VALIDATOR CLAS
class Validator:
    # NAME
    def is_valid_name():
        return True

    # GENDER
    def is_valid_gender():
        return True

    # WEIGHT
    def is_valid_weight():
        return True
#donor
    # DATE
    def is_valid_date(date):
        try:
            valid_date = datetime.strptime(date, "%Y.%m.%d")
            return True
        except:
            return False

    # SICKNESS
    def is_valid_sickness():
        return True

    # ID NUMBER
    def is_valid_id_number():
        return True

    # ID EXPIRATION DATE
    def is_valid_exp_date():
        return True

    # BLOOD TYPE
    def is_valid_blood_type():
        return True

    # EMAIL ADDRESS
    def is_valid_email_address():
        return True

    # MOBILE NUMBER
    def is_valid_mobile_number():
        return True


# INPUT HELPER CLASS
class InputHelper:
    # NAME
    def get_name():
        return name

    # GENDER
    def get_gender():
        return gender

    # WEIGHT
    def get_weight():
        return weight

    # DATE OF BIRTH
    def get_date_of_birth():
        date_of_birth = input("Please enter the donor's date of birth in the following format, 2000.12.31: ")
        v = Validator
        while not v.is_valid_date(date_of_birth):
            print("Wrong format. Try again...")
            date_of_birth = input("Please enter the donor's last donation date in the following format, 2000.12.31: ")
        return date_of_birth

    def get_donation_date():
        donation_date = input("Please enter the donor's last donation date in the following format, 2000.12.31: ")
        v = Validator
        while not v.is_valid_date(donation_date):
            print("Wrong format. Try again...")
            donation_date = input("Please enter the donor's date of birth in the following format, 2000.12.31: ")
        return donation_date

    # SICKNESS
    def get_sickness():
        return sickness

    # ID NUMBER
    def get_id_number():
        return id_number

    # ID EXPIRATION DATE
    def get_exp_date():
        return exp_date

    # BLOOD TYPE
    def get_blood_type():
        return blood_type

    # EMAIL ADDRESS
    def get_email_address():
        return email_address

    # MOBILE NUMBER
    def get_mobile_number():
        return mobile_number
