from os import path
import time
import csv
import os


def if_csv_is_not_exist(file_name):
	"""

	:return:
	"""
	if not (path.isfile(file_name)):
		donors_csv = open(file_name, 'w')
		donors_csv.close()


def check_first_row_and_write(file_name, file_data, first_row):
	"""

	:param file_name:
	:param file_data:
	:param first_row:
	:return:
	"""

	csv_is_empty = True

	with open(file_name, "r") as csv_file:
		first_row_reader = csv.reader(csv_file)
		for row in first_row_reader:
			if len(row) > 0:
				csv_is_empty = False

	if csv_is_empty:
		with open(file_name, "w") as csv_file:
			first_row_writer = csv.writer(csv_file)
			first_row_writer.writerow(first_row)

	with open(file_name, "a") as csv_file:
		append_donor_data = csv.writer(csv_file)
		append_donor_data.writerow(file_data)


def check_if_file_is_empty(file_name, given_row):
	"""

	:param file_name:
	:return:
	"""
	new_list = []
	new_list_len = 0
	csv_is_empty = True

	with open(file_name, "r") as csv_file:
		read_donors_csv = csv.reader(csv_file)
		for row in read_donors_csv:
			if len(row) > 0:
				new_list_len += 1
				new_list.append(row)
				csv_is_empty = False
				if row[given_row] not in ["Event ID", "ID number"]:
					pass

	if csv_is_empty or new_list_len == 1:
		os.system("CLS")
		print("The file is empty!")
		time.sleep(3)
		from main import menu
		menu()
	return new_list