import os


def search_donors(new_list, file_name):
	"""

	:param new_list:
	:return:
	"""

	found_donor_or_event = 0
	row_counter = 0

	if file_name == "Data\donors.csv":
		searched_donor_data = input("Please enter the donor's data for search:")
		for row in new_list:
			for data in row:
				if searched_donor_data in data and row != new_list[0]:
					row_counter += 1
					if found_donor_or_event != 1:
					# if found_donor_or_event == 1:
					# if row_counter % 3 != 0:
						print(row[0], row[1], "\n", row[2], "\n", row[4], "\n", row[11])
						found_donor_or_event += 1
					if found_donor_or_event == 12:
						found_donor_or_event = 0

					# break
					# else:
					# 	answer = input("\nNext page? Press y to continue: ")
					# 	if answer == 'y':
					# 		os.system("CLS")
					# 		row_counter == 0

	if file_name == "Data\events.csv":
		searched_event_data = input("Please enter the event's data for search: ")
		for row in new_list:
			for data in row:
				if searched_event_data in data and row != new_list[0]:
					print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
					found_donor_or_event += 1
					break

	if found_donor_or_event == 0:
		print("Given data is not found!")

	if input("\nTo exit the program press E, to return to the Main menu press Enter: ").upper() == "E":
		os.system("CLS")
		exit()
