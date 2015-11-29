import csv
import time


def delete_donor_data_from_file():
	"""

	:return:
	"""
	csv_is_empty = True
	data_in_donors_csv = []
	data_in_donors_csv_len = 0
	appended_list = []
	appended_list_len = 0

	with open("Data\donors.csv", "r") as donors_csv:
		read_donors_csv = csv.reader(donors_csv)
		print("Existing IDs: \n")
		for row in read_donors_csv:
			if len(row) > 0:
				data_in_donors_csv_len += 1
				data_in_donors_csv.append(row)
				csv_is_empty = False
				print("\t" + row[7])

	if csv_is_empty:
		print("The file is empty!")
		time.sleep(3)
		return False

	id_number = input("\nPlease enter the choosen id that you want to delete: ")

	if id_number == "exit":
		from main import menu
		return False

	for row in data_in_donors_csv:
		if len(row) > 0:
			if id_number != row[7]:
				appended_list_len += 1
				appended_list.append(row)

	if data_in_donors_csv_len != appended_list_len:
		are_you_sure = input("Are you sure? If yes, press y otherwise press any key to go back to the main menu: ")
		if are_you_sure == "y":
			with open("Data\donors.csv", "w") as csv_file:
				csv_writer = csv.writer(csv_file)
				for row in appended_list:
					csv_writer.writerow(row)
					print("Back to the main menu!")
					time.sleep(3)
		else:
			from main import menu

	if appended_list_len == data_in_donors_csv_len:
		print("\nThe given ID is not exist!")
		delete_donor_data_from_file()