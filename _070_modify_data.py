from _011_donor_inputs import *
from _010_add_new_donor import *
user = Donor()


def search_by_id(file):

	if file == "Data\donors.csv":

		with open("Data\donors.csv", "r") as donors:
			donor_id = input("Please enter the ID of the donor that you want to find: ")

			for row in donors:
				if donor_id in row:
					menu = row.split(",")

					print("1.First name: {}".format(menu[0]),
					      "\n2.Last name: {}".format(menu[1]),
					      "\n3.Weight: {}kg".format(menu[2]),
					      "\n4.Gender: {}".format(menu[3]),
					      "\n5.Date of birth: {}".format(menu[4]),
					      "\n6.Last donation date: {}".format(menu[5]),
					      "\n7.Sickness: {}".format(menu[6]),
					      "\n8.ID number: {}".format(menu[7]),
					      "\n9.ID exparitation date: {}".format(menu[8]),
					      "\n10.Blood type: {}".format(menu[9]),
					      "\n11.Email address: {}".format(menu[10]),
					      "\n12.Mobile number: {}".format(menu[11]),
					      "\n13.Hemoglobin level: {}".format(menu[12]))


					# ˇ This probably should be in another function. ˇ

					selecetor = input("Please select which data you want to change"
					                  "\nby entering the corresponding number from the menu here: ")

					if selecetor == "1":
						pass


search_by_id("Data\donors.csv")


# data_to_change = input("Please enter the data that you want to change: ")

def modify_donors(donor_data_list):
	pass


def modify_events(event_list, file):
	pass
