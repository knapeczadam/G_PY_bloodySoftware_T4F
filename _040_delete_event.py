import time
import csv


def delete_event_data_from_file(new_list):
	"""

	:return:
	"""
	new_list_len = 0
	appended_list = []
	appended_list_len = 0

	id_number = input("\nPlease enter the choosen id that you want to delete: ")

	if id_number == "exit":
		return False

	for row in new_list:
		if len(row) > 0:
			new_list_len += 1
			if id_number != row[0]:
				appended_list_len += 1
				appended_list.append(row)

	if new_list_len != appended_list_len:
		are_you_sure = input("Are you sure? If yes, press y otherwise press any key to go back to the main menu: ")
		if are_you_sure == "y":
			with open("Data\events.csv", "w") as csv_file:
				csv_writer = csv.writer(csv_file)
				for row in appended_list:
					csv_writer.writerow(row)
					print("Back to the main menu!")
		else:
			return False

	if appended_list_len == new_list_len:
		print("\nThe given ID is not exist!")
		delete_event_data_from_file(new_list)
