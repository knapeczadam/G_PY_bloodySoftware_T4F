from _011_donor_inputs import Donor
from datetime import datetime
from os import path
import time
import csv
import os

user = Donor()


def call_get_donor_inputs():
	"""

	:return:
	"""
	user.get_first_name()
	user.get_last_name()
	user.get_weight()
	if int(user.weight) <= 50:
		os.system("CLS")
		print("""\
Donors are only accepted above 50 kgs.
The program has ended because of not suitable donor.\
		""")
		time.sleep(3)
		os.system("CLS")
		from main import menu
		menu()
	user.get_gender()
	user.get_date_of_birth()
	if (datetime.now() - datetime.strptime(user.date_of_birth, "%Y.%m.%d")).days // 365 < 18:
		os.system("CLS")
		print("""\
Donors are only accepted above 18 years.
The program has ended because of not suitable donor.\
		""")
		time.sleep(3)
		exit()
	user.get_donation_date()
	if user.donation_date != "" and (datetime.now() - datetime.strptime(user.donation_date, "%Y.%m.%d")).days <= 90:
		os.system("CLS")
		print("""\
Donors can only give blood once in every 3 months.\
The program has ended because of not suitable donor.
		""")
		time.sleep(3)
		exit()
	user.get_sickness()
	if user.sickness.lower() == "y":
		os.system("CLS")
		print("The program has ended because of not suitable donor.")
		time.sleep(3)
		exit()
	user.get_id_number()
	#
	user.get_exp_date()
	if datetime.strptime(user.exp_date, "%Y.%m.%d") < datetime.now():
		os.system("CLS")
		print("The donor's ID is expired! Program is shutting down...")
		time.sleep(3)
		exit()
	user.get_blood_type()
	user.get_email_address()
	user.get_mobile_number()


def write_donor_data_in_file():
	donor_date = [user.first_name,\
				  user.last_name,\
				  user.weight,\
				  user.gender,\
				  user.date_of_birth,\
				  user.donation_date,\
				  user.sickness,\
				  user.id_number,\
				  user.exp_date,\
				  user.blood_type,\
				  user.email_address,\
				  user.mobile_number]
	if not (path.isfile("Data\donors.csv")):
		f = open("Data\donors.csv", 'w')
		f.close()
	data = []
	with open("Data\donors.csv") as csvfile_read:
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
	print("The donor's data has been recorded.")
	with (open("Data\donors.csv", 'w')) as writer:
		csvwriter = csv.writer(writer, delimiter=",")
		for word in dicta:
			csvwriter.writerow(dicta[word])
	with open("Data\donors.csv", "a") as csvfile_write:
		csvwriter = csv.writer(csvfile_write, delimiter=',')
		csvwriter.writerow(donor_date)
		print("New donor:", donor_date)
