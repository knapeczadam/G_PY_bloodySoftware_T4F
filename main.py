#!/usr/bin/env python
# -*- coding: utf-8 -*-
from donor import DonorInputHelper
from event import EventInputHelper
from datetime import datetime

# Welcomes to the program and starts an option.
print("Welcome to the blood donation program.\n")
d_e_s = ""
d_e_s_list = ["D", "E", "S", "d", "e", "s"]
# Keeps asking the user which program option to run till one of the above listed letters is chosen.
while d_e_s not in d_e_s_list:
    d_e_s = input("To start a Donor registration press D; \
                    \nTo start an Event registration press E; \
                    \nTo Stop the program press S: ")

# DONOR REGISTRATION
# In case D is entered, calls all the Donor definitions.
if d_e_s.upper() == "D":
    DonorInputHelper.get_name()
    DonorInputHelper.get_gender()
    # If the returned number from the def is not greater than 50, the program stops.
    if int(DonorInputHelper.get_weight()) <= 50:
        print("\nDonors are only accepted above 50 kgs.")
        print("The program has ended because of not suitable donor.")
        exit()
    # If the returned date from the def is within 18 years of the current date, the program stops.
    if (datetime.now() - datetime.strptime(DonorInputHelper.get_date_of_birth(), "%Y.%m.%d")).days // 365 < 18:
        print("\nDonors are only accepted above 18 years.")
        print("The program has ended because of not suitable donor.")
        exit()
    # If the returned date from the def is within 90 days of the current date, the program stops.
    if (datetime.now() - datetime.strptime(DonorInputHelper.get_donation_date(), "%Y.%m.%d")).days <= 90:
        print("\nDonors can only give blood once in every 3 months.")
        print("The program has ended because of not suitable donor.")
        exit()
    if DonorInputHelper.get_sickness().lower() == "y":
        print("-----")
        print("The program has ended because of not suitable donor.")
        exit()
    DonorInputHelper.get_id_number() #elobb vagy utan
    if datetime.strptime(DonorInputHelper.get_exp_date(), "%Y.%m.%d") < datetime.now():
        print("Lejart")
        exit()
    DonorInputHelper.get_blood_type()
    DonorInputHelper.get_email_address()
    DonorInputHelper.get_mobile_number()
    print("The donor's data is recorded.")

# EVENT REGISTRATION
# In case E is entered, calls all the Event definitions.
elif d_e_s.upper() == "E":
    EventInputHelper.get_date_of_event()
    EventInputHelper.get_start_time()
    EventInputHelper.get_end_time()
    EventInputHelper.get_zip_code()
    EventInputHelper.get_city()
    EventInputHelper.get_address()
    EventInputHelper.get_available_beds()
    EventInputHelper.calc_max_donor_number()
    EventInputHelper.get_planned_donor_number()
    if float(EventInputHelper.get_succesfull_donations())\
            / float(EventInputHelper.get_planned_donor_number()) < 0.2:
        print("Unsuccessfull, not worths to organise there again")
    if 0.2 <= float(EventInputHelper.get_succesfull_donations())\
            / float(EventInputHelper.get_planned_donor_number()) <= 0.75:
        print("Normal event")
    if 0.75 <= float(EventInputHelper.get_succesfull_donations())\
            / float(EventInputHelper.get_planned_donor_number()) <= 1.1:
        print("Successfull")
    if float(EventInputHelper.get_succesfull_donations())\
            / float(EventInputHelper.get_planned_donor_number()) > 1.1:
        print("Outstanding")

# In case S is entered, the program stops.
elif d_e_s.upper() == "S":
    print("The program ended normally.")
    exit()
