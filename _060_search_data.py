import csv


def search_donors():

	data_in_donors_csv = []

	with open("Data\donors.csv", "r") as donors_csv:
		csv_reader = csv.reader(donors_csv)
		for row in csv_reader:
			if row != 0:
				data_in_donors_csv.append(row)

	print(data_in_donors_csv)
	searched_data = input("Please enter the donor's data for search: ")

	for row in data_in_donors_csv:
		if searched_data in row:
			print(row)

	if input("\nTo exit the program press E, to return to the Main menu press Enter: ").upper() == "E":
		exit()
