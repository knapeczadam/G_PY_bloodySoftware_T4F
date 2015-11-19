#!/usr/bin/env python
# -*- coding: utf-8 -*-
from donor import DonorInputHelper
from event import EventInputHelper
from datetime import datetime

Event_data = []
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
    name = DonorInputHelper.get_name()
    gender = DonorInputHelper.get_gender()
    # If the returned number from the def is not greater than 50, the program stops.
    weight = DonorInputHelper.get_weight()
    if int(weight) <= 50:
        print("\nDonors are only accepted above 50 kgs.")
        print("The program has ended because of not suitable donor.")
        exit()
    # If the returned date from the def is within 18 years of the current date, the program stops.
    age = DonorInputHelper.get_date_of_birth()
    if (datetime.now() - datetime.strptime(age, "%Y.%m.%d")).days // 365 < 18:
        print("\nDonors are only accepted above 18 years.")
        print("The program has ended because of not suitable donor.")
        exit()
    # If the returned date from the def is within 90 days of the current date, the program stops.
    last_don = DonorInputHelper.get_donation_date()
    if (datetime.now() - datetime.strptime(last_don, "%Y.%m.%d")).days <= 90:
        print("\nDonors can only give blood once in every 3 months.")
        print("The program has ended because of not suitable donor.")
        exit()
    sick = DonorInputHelper.get_sickness()
    if sick.lower() == "y":
        print("-----")
        print("The program has ended because of not suitable donor.")
        exit()
    id_code = DonorInputHelper.get_id_number()
    #elobb vagy utan
    exp_date = DonorInputHelper.get_exp_date()
    if datetime.strptime(exp_date, "%Y.%m.%d") < datetime.now():
        print("Lejart")
        exit()
    blood = DonorInputHelper.get_blood_type()
    email = DonorInputHelper.get_email_address()
    mobile = DonorInputHelper.get_mobile_number()
    print("The donor's data is recorded.")
    Donor_data = [name, gender, weight, age, last_don, sick, id_code, exp_date, blood, email, mobile]
    print(Donor_data)

# EVENT REGISTRATION
# In case E is entered, calls all the Event definitions.
elif d_e_s.upper() == "E":
    EventInputHelper.get_event_date()
    EventInputHelper.get_donation_start()
    EventInputHelper.get_donation_end()
    EventInputHelper.get_zip_code()
    EventInputHelper.get_city()
    EventInputHelper.get_address()
    EventInputHelper.get_available_beds()
    EventInputHelper.get_max_donor_number()
    EventInputHelper.get_planned_donor_number()
    if float(EventInputHelper.get_succesfull_donations()) / float(EventInputHelper.get_planed_don_num()) < 0.2:
        print("Unsuccessfull, not worths to organise there again")
    if 0.2 <= float(EventInputHelper.get_succesfull_donations()) / float(EventInputHelper.get_planed_don_num()) <= 0.75:
        print("Normal event")
    if 0.75 <= float(EventInputHelper.get_succesfull_donations()) / float(EventInputHelper.get_planed_don_num()) <= 1.1:
        print("Successfull")
    if float(EventInputHelper.get_succesfull_donations()) / float(EventInputHelper.get_planed_don_num()) > 1.1:
        print("Outstanding")

# In case S is entered, the program stops.
elif d_e_s.upper() == "S":
    print("The program ended normally.")
    exit()
