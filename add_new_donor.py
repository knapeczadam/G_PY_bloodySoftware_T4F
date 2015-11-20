from donor_inputs import DonorInputHelper
from datetime import datetime
import csv

class AddNewDonor:
	main_do_name = DonorInputHelper.get_name()
	main_do_gender = DonorInputHelper.get_gender()
	main_do_weight = DonorInputHelper.get_weight()
	# If the returned number from the def is not greater than 50, the program stops.
	if int(main_do_weight) <= 50:
		print("\nDonors are only accepted above 50 kgs.")
		print("The program has ended because of not suitable donor.")
		exit()
	main_do_birth = DonorInputHelper.get_date_of_birth()
	# If the returned date from the def is within 18 years of the current date, the program stops.
	if (datetime.now() - datetime.strptime(main_do_birth, "%Y.%m.%d")).days // 365 < 18:
		print("\nDonors are only accepted above 18 years.")
		print("The program has ended because of not suitable donor.")
		exit()
	main_do_last_don = DonorInputHelper.get_donation_date()
	# If the returned date from the def is within 90 days of the current date, the program stops.
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
	main_do_exp_id = DonorInputHelper.get_exp_date()
	if datetime.strptime(main_do_exp_id, "%Y.%m.%d") < datetime.now():
		print("The donor's ID is expired! Program is shutting down...")
		exit()
	main_do_blood = DonorInputHelper.get_blood_type()
	main_do_email = DonorInputHelper.get_email_address()
	main_do_mobile = DonorInputHelper.get_mobile_number()

	@staticmethod
	def write_donor_data_infile():
		Donor_data = [AddNewDonor.main_do_name, AddNewDonor.main_do_gender, AddNewDonor.main_do_weight, AddNewDonor.main_do_birth, AddNewDonor.main_do_last_don, AddNewDonor.main_do_sick, AddNewDonor.main_do_id,
				AddNewDonor.main_do_exp_id, AddNewDonor.main_do_blood, AddNewDonor.main_do_email, AddNewDonor.main_do_mobile]
		# existing_data = []
		#
		# with open("Data\donors.csv") as csvfile_read:
		# 	csvreader = csv.reader(csvfile_read, delimiter=",")
		# 	for row in csvreader:
		# 		if row:
		# 			existing_data.append(row)
		# csvfile_read.close()

		dicta = {}
		x = 1
		for elements in Donor_data:
			dicta[x] = elements
			x += 1
		print(dicta)

		# delete = input("Would you like to pop an item?")
		# if delete:
		# 	if delete.isdigit:
		# 		dicta.pop(int(delete))
		print("The donor's data has been recorded.")

		with (open("Data\donors.csv", 'w')) as writer:
			csvwriter = csv.writer(writer, delimiter=",")
			csvwriter.writerow(Donor_data)

		z = input("Do you want to clear the donors data file? (Y/N)")
		if z.lower() == "y":
			open("Data\donors.csv", 'w').close()
			print("The donors data file has been cleared!")

	# @staticmethod
	# def delete_donor_data_fromfile():
	#
	# 	data = []
	#
	# 	with open("Data\donors.csv") as csvfile_read:
	# 		csvreader = csv.reader(csvfile_read, delimiter=",")
	# 		for row in csvreader:
	# 			if row:
	# 				data.append(row)
	# 	csvfile_read.close()
	#
	# 	dicta = {}
	# 	x = 1
	# 	for elements in data:
	# 		dicta[x] = elements
	# 		x += 1
	# 	print(dicta)
	#
	# 	delete = input("Would you like to delete an item?")
	# 	if delete:
	# 		if delete.isdigit:
	# 			dicta.pop(int(delete))
	#
	# 	print(dicta)
	# 	with (open("Data\donors.csv", 'w')) as writer:
	# 		csvwriter = csv.writer(writer, delimiter=",")
	# 		for word in dicta:
	# 			csvwriter.writerow(dicta[word])
	#
	# 	with open("Data\donors.csv", "a") as csvfile_write:
	# 		csvwriter = csv.writer(csvfile_write, delimiter=',')
	# 		csvwriter.writerow(Donor_data)
	# 		print("New donor:", Donor_data)
	#
	# 	z = input("Do you want to clear the donors data file? (Y/N)")
	# 	if z.lower() == "y":
	# 		open("Data\donors.csv", 'w').close()
	# 		print("The donors data file has been cleared!")
	#
	#
	# Donor_data = [main_do_name, main_do_gender, main_do_weight, main_do_birth, main_do_last_don, main_do_sick, main_do_id,
	# 			  main_do_exp_id, main_do_blood, main_do_email, main_do_mobile]
	# print(Donor_data)
