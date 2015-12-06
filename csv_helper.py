from os import path
import time
import csv

HEADER_INDEX = 0


def if_csv_is_not_exist(file_path: str):
	"""
	This function checks the csv's path. If it isn't exist, create a new one.
	:param file_path:
	:return: a created file in a folder
	"""
	if not (path.isfile(file_path)):
		donors_csv = open(file_path, 'w')
		donors_csv.close()


def check_first_row_and_write(file_path: str, first_row: list):
	"""
	This function checks the csv's header. If header isn't exist create a new one.
	After header creating new donor or event data appends after last row of given file.
	:param file_path:
	:param new_donor_or_event:
	:param first_row: Header of donor's or event's csv
	:return: csv file with appended data
	"""
	first_row_exists = False
	with open(file_path, "r") as csv_file:
		first_row_reader = csv.reader(csv_file)
		for row in first_row_reader:
			if len(row) > 0:
				first_row_exists = True

	if not first_row_exists:
		with open(file_path, "w") as csv_file:
			first_row_writer = csv.writer(csv_file)
			first_row_writer.writerow(first_row)


def append_new_donor_or_event_to_csv(file_path: str, new_donor_or_event: list):
	"""

	:param file_path:
	:param new_donor_or_event:
	:return:
	"""
	with open(file_path, "a") as csv_file:
		new_data_writer = csv.writer(csv_file)
		new_data_writer.writerow(new_donor_or_event)


def file_is_empty(file_path: str):
	"""
	This function checks the csv file's rows. If it contains any rows - including header - returns a bool
	:param file_path: Path of the current csv file
	:return: bool
	"""
	row_counter = 0
	with open(file_path, "r") as csv_file:
		read_given_csv = csv.reader(csv_file)
		for row in read_given_csv:
			row_counter += 1
	if row_counter < 3:
		print("The file is empty! Back to the main menu...")
		time.sleep(1)
		return True


def pure_data_from_csv_file(file_path: str):
	"""
	This function reads each rows of the given csv file and appends every rows to a new list without header
	:param file_path:
	:return: list
	"""
	pure_data = []
	with open(file_path, "r") as csv_file:
		read_given_csv = csv.reader(csv_file)
		for index, row in enumerate(read_given_csv):
			if index != HEADER_INDEX:
				if len(row) > 0:
					pure_data.append(row)
	return pure_data
