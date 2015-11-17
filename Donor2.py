#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from datetime import datetime
from sys import exit
# Imports the sys.exit command. In case of wrong data it exits.

enter = "Enter your"  # An abbrevation.


def get_input():
    global Input
    Input = input("Please %s : " % enter)
    return Input


class DonorData():
    """

    # ID EXPIRATION DATE
    @staticmethod
    def get_exp_date():
        global date_of_exp   # Can be used outside the definition.
        isvaild = False  # A variable for try/except.
        while not isvaild:
            data = input("Please enter the donor's ID expiration date in the following format, 2000.12.31: ")
            try:
                date_of_exp = datetime.strptime(data, "%Y.%m.%d")  # Only let the data pass if it matches this format.
                if date_of_exp > datetime.now():
                    isvaild = True
                elif date_of_exp < datetime.now():
                    date_of_exp = False
                    return False
            except:
                print("Wrong format. Please try again in the following format, 2000.12.31: ")
        return date_of_exp

    # HEMOGLOBIN LEVEL
    # Generates a random number: hemogblobin level between 80-200, that must be higher than 110.
    @staticmethod
    def hemo_level():
        global level # Can be used outside the definition
        level = (random.randrange(80, 200))  # generates a number between 80 and 200.
        if level > 110:
            return level  # If it is greater than 110, return with it.
        else:
            exit("Your Hemogblobin level is not high enough.")  # If it is lesser than 110, it exits.

    # EMAIL ADDRESS
    @staticmethod
    # Email address
    def get_email_address():  # The function asks for a valid email address
        global email_address
        isvalid = False
        while not isvalid:
            email_address = input("%s email address: " % enter)
            email_address_string = email_address.replace(" ", "")
            contains_at_sign = "@" in email_address_string and email_address_string.index("@") > 0
            ending_is_valid = email_address_string.endswith(".hu") or email_address_string.endswith(".com")
            isvalid = contains_at_sign and ending_is_valid
            if not isvalid:     # If it's not a valid address, the user gets this message.
                print("The given '%s' email address is not in a valid format!" % email_address)
            if not contains_at_sign:        # If the address misses an '@' sign, the user gets this message as well.
                print("Please add an '@' sign in your address!")
            if not ending_is_valid:                               # If the address misses the email providers location,
                print("Please specify where your email provider is ('.com' or '.hu')!")   # the user gets this message.
        return email_address

       # ID NUMBER
    # Asks the donor's unique identifier and determines whether it suggests a national ID or a passport.
    @staticmethod
    def get_id_number():
        id_number = ""
        # Asks for the ID number here first.
        id_number = input("Please enter the donor's ID number: ")
        # Keeps asking for the input while it is not 8 characters long and only alphanumeric.
        while len(id_number) != 8 or not id_number.isalnum():
            id_number = input("Wrong format. The ID has to be 8 characters long and contain only letters and numbers: ")
        # Decides whether the given string suggests a national ID number or a passport number.
        if id_number[:6].isdigit() and id_number[6:].isalpha():
            print("Your ID number is recorded.")
        elif id_number[:6].isalpha() and id_number[6:].isdigit():
            print("Your passport number is recorded.")
        else:
            # If it does not match any of the two mentioned, it says so too.
            print("The format of your ID number could not be defined, however it was recorded.")
        # Returns with the ID number.
        return id_number


        """




    def get_weight(self):

        return str(self).isdigit() or str(self) == ""

    def get_name(self):
        split_Name = str(self).split(" ")
        return str(self).replace(" ", "").isalpha() and len(split_Name) > 1

    def get_birth(self):
        while True:
            try:
                date_of_birth = datetime.strptime(self, "%Y.%m.%d")
                return True
            except:
                return False

    def get_donation(self):
        while True:
            try:
                date_of_don = datetime.strptime(self, "%Y.%m.%d")
                return True
            except:
                return False

    def get_gender(self):
        available_genders = ["f", "m"]
        if str(self).lower() in available_genders:
            return True
        else:
            return False

    def get_sickness(self):
        yes_or_no = ["y", "n"]
        if str(self).lower() in yes_or_no:
            return True
        else:
            return False

    def get_blood(self):
        Blood_types = ["a", "b", "ab", "0"]
        if str(self).lower() in Blood_types:
            return True
        else:
            return False

    def get_mobile_number(self):

        mobile_string = self.replace(" ", "")

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

enter = "Enter your Blood"
def get_blood():

    while DonorData.get_blood(get_input()) is False:
        print("Again")
    return Input

enter = "Enter your Weight"
def get_weight():

    while DonorData.get_weight(get_input()) is False:
        print("Again")
    return Input

enter = "Enter your Full Name"
def get_name():

    while DonorData.get_name(get_input()) is False:
        print("Again")
    return Input

enter = "Enter your Bday"
def get_birth():

    while DonorData.get_birth(get_input()) is False:
        print("Again")
    return Input

enter = "Enter your DonDay"
def get_don():

    while DonorData.get_donation(get_input()) is False:
        print("Again")
    return Input

enter = "Enter your Gender"
def get_gen():

    while DonorData.get_gender(get_input()) is False:
        print("Again")
    return Input

enter = "Enter your Sick"
def get_sick():

    while DonorData.get_sickness(get_input()) is False:
        print("Again")
    return Input

enter = "Enter your Mobile"
def get_mobile():

    while DonorData.get_mobile_number(get_input()) is False:
        print("Again")
    return Input


