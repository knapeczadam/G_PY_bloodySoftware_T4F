#!/usr/bin/env python
# -*- coding: utf-8 -*-
from donor import DonorInputHelper
from event import EventInputHelper
from datetime import datetime
import csv

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
    data = []

    with open("donor.csv") as csvfile_read:
        csvreader = csv.reader(csvfile_read, delimiter=",")
        for row in csvreader:
            if row:
                data.append(row)
    csvfile_read.close()
    dicta = {}
    x = 1
    for elements in data:
        dicta[x] = elements
        x += 1
    print(dicta)

    delete = input("Whould you like to pop an item?")
    if delete:
        if delete.isdigit:
            dicta.pop(int(delete))
    main_do_name = DonorInputHelper.get_name()
    main_do_gender = DonorInputHelper.get_gender()
    # If the returned number from the def is not greater than 50, the program stops.
    main_do_weight = DonorInputHelper.get_weight()
    if int(main_do_weight) <= 50:
        print("\nDonors are only accepted above 50 kgs.")
        print("The program has ended because of not suitable donor.")
        exit()
    # If the returned date from the def is within 18 years of the current date, the program stops.
    main_do_birth = DonorInputHelper.get_date_of_birth()
    if (datetime.now() - datetime.strptime(main_do_birth, "%Y.%m.%d")).days // 365 < 18:
        print("\nDonors are only accepted above 18 years.")
        print("The program has ended because of not suitable donor.")
        exit()
    # If the returned date from the def is within 90 days of the current date, the program stops.
    main_do_last_don = DonorInputHelper.get_donation_date()
    if (datetime.now() - datetime.strptime(main_do_last_don, "%Y.%m.%d")).days <= 90:
        print("\nDonors can only give blood once in every 3 months.")
        print("The program has ended because of not suitable donor.")
        exit()
    main_do_sick = DonorInputHelper.get_sickness()
    if main_do_sick.lower() == "y":
        print("-----")
        print("The program has ended because of not suitable donor.")
        exit()
    main_do_id = DonorInputHelper.get_id_number()
    #elobb vagy utan
    main_do_exp_id = DonorInputHelper.get_exp_date()
    if datetime.strptime(main_do_exp_id, "%Y.%m.%d") < datetime.now():
        print("Lejart")
        exit()
    main_do_blood = DonorInputHelper.get_blood_type()
    main_do_email = DonorInputHelper.get_email_address()
    main_do_mobile = DonorInputHelper.get_mobile_number()
    print("The donor's data is recorded.")
    Donor_data = [main_do_name, main_do_gender, main_do_weight, main_do_birth, main_do_last_don, main_do_sick, main_do_id, main_do_exp_id, main_do_blood, main_do_email, main_do_mobile]
    print(Donor_data)

    data = []

    with open("donor.csv") as csvfile_read:
        csvreader = csv.reader(csvfile_read, delimiter=",")
        for row in csvreader:
            if row:
                data.append(row)
    csvfile_read.close()
    dicta = {}
    x = 1
    for elements in data:
        dicta[x] = elements
        x += 1
    print(dicta)

    delete = input("Whould you like to pop an item?")
    if delete:
        if delete.isdigit:
            dicta.pop(int(delete))

    print(dicta)
    with (open("donor.csv", 'w')) as writer:
        csvwriter = csv.writer(writer, delimiter=",")
        for word in dicta:
            csvwriter.writerow(dicta[word])
    with open("donor.csv", "a") as csvfile_write:
        csvwriter = csv.writer(csvfile_write, delimiter=',')
        csvwriter.writerow(Donor_data)
        print("New:", Donor_data)

    z = input("Wanna clear your csv? (Y/N)")
    if z.lower() == "y":
        open("donor.csv", 'w').close()
        print("Cleared!")

# EVENT REGISTRATION
# In case E is entered, calls all the Event definitions.
elif d_e_s.upper() == "E":
    main_ev_date_of_event = EventInputHelper.get_date_of_event()
    main_ev_start_time = EventInputHelper.get_start_time()
    main_ev_end_time = EventInputHelper.get_end_time()
    main_ev_zip_code = EventInputHelper.get_zip_code()
    main_ev_city = EventInputHelper.get_city()
    main_ev_address = EventInputHelper.get_address()
    main_ev_beds = EventInputHelper.get_available_beds()
    main_ev_don_num = EventInputHelper.calc_max_donor_number()
    main_ev_plan_don_num = EventInputHelper.get_planned_donor_number()
    main_ev_succ_don = EventInputHelper.get_succesfull_donations()
    if float(main_ev_succ_don)\
            / float(main_ev_plan_don_num) < 0.2:
        print("Unsuccessfull, not worths to organise there again")
    if 0.2 <= float(main_ev_succ_don)\
            / float(main_ev_plan_don_num) <= 0.75:
        print("Normal event")
    if 0.75 <= float(main_ev_succ_don)\
            / float(main_ev_plan_don_num) <= 1.1:
        print("Successfull")
    if float(main_ev_succ_don)\
            / float(main_ev_plan_don_num) > 1.1:
        print("Outstanding")

# In case S is entered, the program stops.
elif d_e_s.upper() == "S":
    print("The program ended normally.")
    exit()
