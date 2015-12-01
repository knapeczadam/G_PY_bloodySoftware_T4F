import csv
import os


def search_donors():

	data_in_donors_csv = []

	with open("Data\donors.csv", "r") as donors_csv:
		csv_reader = csv.reader(donors_csv)
		for row in csv_reader:
			if len(row) != 0:
				data_in_donors_csv.append(row)

	searched_data = input("Please enter the donor's data for search: ")

	found_donor = 0

	for row in data_in_donors_csv:
		for data in row:
			if searched_data in data and row != data_in_donors_csv[0]:
				print(row[0], row[1], "\n", row[2], "\n", row[4], "\n", row[11])
				found_donor += 1
				break

	if found_donor == 0:
		print("Donor not found!")

	if input("\nTo exit the program press E, to return to the Main menu press Enter: ").upper() == "E":
		os.system("CLS")
		exit()
