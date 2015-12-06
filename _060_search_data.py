import os


def search_data(pure_data, string_name, page_number):
	"""

	:param pure_data:
	:return:
	"""
	found_donor_or_event = False
	founded_data = []

	searched_data = input("Please enter the {}'s data for search: ".format(string_name))
	for row in pure_data:
		for element in row:
			if searched_data in element:
				found_donor_or_event = True
				founded_data.append(row)
				break
	row_counter = 1
	for row in founded_data:
		if row_counter % page_number == 0:
			answer = input("\nNext page? Press any key to continue: ")
			if answer:
				os.system("CLS")
				row_counter = 0
		if string_name == "Donor":
			row_counter += 1
			printing_after_donor_search(row)
		if string_name == "Event":
			row_counter += 1
			printing_after_event_search(row)
	if not found_donor_or_event:
		print("Given data is not found!")
		search_data(pure_data, string_name, page_number)
	if input("\nTo exit the program press E, to return to the Main menu press any key: ").upper() == "E":
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