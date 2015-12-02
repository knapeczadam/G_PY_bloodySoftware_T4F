from _datetime import datetime
from operator import itemgetter
import os


def list_donor_data(listed_donor_data, sorted_by_index):
	"""

	:param data:
	:return:
	"""
	dicta = {}
	x = 1
	for elements in sorted(listed_donor_data,key=itemgetter(sorted_by_index)):
		dicta[x] = elements
		x += 1

	row_counter = 0

	for key in dicta:
		if key != 1:
			row_counter += 1
			print("\n", "-" * 40, "\n")
			print("{}, {}".format(dicta[key][1], dicta[key][0]))
			print("{} kg".format(dicta[key][2]))
			year = datetime.strptime(dicta[key][4], "%Y.%m.%d")
			today = datetime.now()
			age = ((today - year).days//365)
			print("{} - {} years old".format(dicta[key][4], age))
			print("{}".format(dicta[key][10]))
			if row_counter % 4 == 0:
				answer = input("\nNext page? Press y to continue: ")
				if answer == 'y':
					os.system("CLS")
					row_counter == 0


def list_event_data(listed_event_data, sorted_by_index):
	"""

	:param data:
	:return:
	"""
	dicta = {}
	x = 1
	for elements in sorted(listed_event_data,key=itemgetter(sorted_by_index)):
		dicta[x] = elements
		x += 1

	row_counter = 0

	for key in dicta:
		if key != 1:
			row_counter += 1
			print("\n", "-" * 40, "\n")
			print("Event ID: {}".format(dicta[key][0]))
			print("Date of Event: {}".format(dicta[key][1]))
			print("Start time: {}".format(dicta[key][2]))
			print("End time: {}".format(dicta[key][3]))
			print("Zip code: {}".format(dicta[key][4]))
			print("City: {}".format(dicta[key][5]))
			print("Address: {}".format(dicta[key][6]))
			print("Available beds: {}".format(dicta[key][7]))
			print("Planned donors: {}".format(dicta[key][8]))
			print("Max donor numbers: {}".format(dicta[key][9]))
			print("Successful donations: {}".format(dicta[key][10]))
			if row_counter % 3 == 0:
				answer = input("\nNext page? Press y to continue: ")
				if answer == 'y':
					os.system("CLS")
					row_counter == 0