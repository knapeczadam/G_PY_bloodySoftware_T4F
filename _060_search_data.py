import os


def search_data(new_list, donor_or_event):
	"""

	:param new_list:
	:return:
	"""

	found_donor_or_event = 0
	row_counter = 0

	searched_donor_data = input("Please enter the {}'s data for search: ".format(donor_or_event))
	for row in new_list:
		for element in row:
			if searched_donor_data in element and row != new_list[0]:
				found_donor_or_event += 1
				row_counter += 1
				if row_counter % 3 == 0 and row_counter != 0:
					if donor_or_event == "Donor":
						printing_after_donor_search(row)
					if donor_or_event == "Event":
						printing_after_event_search(row)
					answer = input("\nNext page? Press y to continue: ")
					if answer == 'y':
						os.system("CLS")
						row_counter = 0
						break
				else:
					if row_counter != 0:
						if donor_or_event == "Donor":
							printing_after_donor_search(row)
						if donor_or_event == "Event":
							printing_after_event_search(row)
							break

	if found_donor_or_event == 0:
		print("Given data is not found!")

	if input("\nTo exit the program press E, to return to the Main menu press Enter: ").upper() == "E":
		os.system("CLS")
		exit()


def printing_after_donor_search(row):
	print(row[0], row[1], "\n", row[2], "\n", row[4], "\n", row[11])


def printing_after_event_search(row):
	print("\n", "-" * 40, "\n")
	print("Event ID: {}".format(row[0]))
	print("Date of Event: {}".format(row[1]))
	print("Start time: {}".format(row[2]))
	print("End time: {}".format(row[3]))
	print("Zip code: {}".format(row[4]))
	print("City: {}".format(row[5]))
	print("Address: {}".format(row[6]))
	print("Available beds: {}".format(row[7]))
	print("Planned donors: {}".format(row[8]))
	print("Max donor numbers: {}".format(row[9]))
	print("Successful donations: {}".format(row[10]))