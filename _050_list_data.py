from _datetime import datetime
from operator import itemgetter
from _060_search_data import printing_after_event_search
import os


def list_donor_data(listed_donor_data, sorted_by_index):
	"""

	:param data:
	:return:
	"""
	row_counter = 0

	for row in sorted(listed_donor_data, key=itemgetter(sorted_by_index)):
		row_counter += 1
		print("\n", "-" * 40, "\n")
		print("{}, {}".format(row[1], row[0]))
		print("{} kg".format(row[2]))
		year = datetime.strptime(row[4], "%Y.%m.%d")
		today = datetime.now()
		age = ((today - year).days//365)
		print("{} - {} years old".format(row[4], age))
		print("{}".format(row[10]))
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
	row_counter = 0

	for row in sorted(listed_event_data,key=itemgetter(sorted_by_index)):
		row_counter += 1
		printing_after_event_search(row)
		if row_counter % 3 == 0:
			answer = input("\nNext page? Press y to continue: ")
			if answer == 'y':
				os.system("CLS")
				row_counter == 0