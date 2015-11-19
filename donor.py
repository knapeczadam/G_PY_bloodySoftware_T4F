from datetime import datetime


<<<<<<< HEAD
# VALIDATOR CLAS
class Validator:
    # NAME
    def validate_name():
        result = None
        userinput = input()
        for char in userinput:
            if char.isalpha() or char == " ":
                result = userinput
            else:
                result = False
        return result

    # GENDER
    def validate_gender():
        result = None
        userinput = input()
        if len(userinput) == 1:
            if userinput == "m" or userinput == "f":
                result = userinput
            else:
                result = False
        else:
            result = False
        return result

    # WEIGHT
    def is_valid_weight():
        return True
=======
# VALIDATOR CLASS
class DonorValidator:
    # NAME
    def is_valid_name(self):
        split_Name = str(self).split(" ")
        return str(self).replace(" ", "").isalpha() and len(split_Name) > 1

    # GENDER
    def is_valid_gender(self):
        available_genders = ["f", "m"]
        return str(self).lower() in available_genders

    # WEIGHT
    def is_valid_weight(self):
        return str(self).isdigit()
>>>>>>> 2c2305445a01963cca4c046a91dcb2b5ca364b73

    # DATE
    def is_valid_date(date):
        try:
<<<<<<< HEAD
            valid_date = datetime.strptime(date, "%Y.%m.%d")
=======
            datetime.strptime(date, "%Y.%m.%d")
>>>>>>> 2c2305445a01963cca4c046a91dcb2b5ca364b73
            return True
        except:
            return False

    # SICKNESS
<<<<<<< HEAD
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
=======
    def is_valid_sickness(self):
        yes_or_no = ["y", "n"]
        return str(self).lower() in yes_or_no

    # ID NUMBER
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
    def is_valid_blood_type(self):
        Blood_types = ["a", "b", "ab", "0"]
        return str(self).lower() in Blood_types

    # EMAIL ADDRESS
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
>>>>>>> 2c2305445a01963cca4c046a91dcb2b5ca364b73
        return True


# INPUT HELPER CLASS
<<<<<<< HEAD
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
=======
class DonorInputHelper:
    def Input():
        global Input
        Input = input(":")
        return Input
    # NAME
    def get_name():
        print("PLS your name:")
        while DonorValidator.is_valid_name(DonorInputHelper.Input()) is False:
            print("AGAIN YOUR NAME:")
        return Input

    # GENDER
    def get_gender():
        print("PLS YOUR F/M:")
        while DonorValidator.is_valid_gender(DonorInputHelper.Input()) is False:
            print("AGAIN YOUR F/M:")
        return Input

    # WEIGHT
    def get_weight():
        print("YOUR KILOGRAMMM:")
        while DonorValidator.is_valid_weight(DonorInputHelper.Input()) is False:
            print("AGAIN YOUR GK:")
        return Input

    # DATE OF BIRTH
    def get_date_of_birth():
        print("Please enter the donor's date of birth in the following format, 2000.12.31: ")
        while DonorValidator.is_valid_date(DonorInputHelper.Input()) is False:
            print("Wrong format. Try again...")
        return Input

    def get_donation_date():
        print("Please enter the donor's last donation date in the following format, 2000.12.31: ")
        while DonorValidator.is_valid_date(DonorInputHelper.Input()) is False:
            print("Wrong format. Try again...")
        return Input

    # SICKNESS
    def get_sickness():
        print("YOU WAS SICK? Y/N")
        while DonorValidator.is_valid_sickness(DonorInputHelper.Input()) is False:
            print("SICK U KNOW:")
        return Input

    # ID NUMBER
    def get_id_number():
        print("YOUR ID PLS(PASS OR ID)")
        while DonorValidator.is_valid_id_number(DonorInputHelper.Input()) is False:
            print("ID is 8 DIGIT!:")
        return Input

    # ID EXPIRATION DATE
    def get_exp_date():
        print("Enter your id exp date")
        while DonorValidator.is_valid_date(DonorInputHelper.Input()) is False:
            print("DATE IS NOT GOOD")
        return Input

    # BLOOD TYPE
    def get_blood_type():
        print("PLS ENTER YOUR BLOOD TYPE")
        while DonorValidator.is_valid_blood_type(DonorInputHelper.Input()) is False:
            print("YOUR BLOOD I SAID")
        return Input

    # EMAIL ADDRESS
    def get_email_address():
        print("YOUR EMAIL PLS")
        while DonorValidator.is_valid_email_address(DonorInputHelper.Input()) is False:
            print("Email pls...:")
        return Input

    # MOBILE NUMBER
    def get_mobile_number():
        print("YOU PHONE NUMBER PLS:")
        while DonorValidator.is_valid_mobile_number(DonorInputHelper.Input()) is False:
            print("M-O-B-I-L-E NUMBER PLS")
        return Input
>>>>>>> 2c2305445a01963cca4c046a91dcb2b5ca364b73
