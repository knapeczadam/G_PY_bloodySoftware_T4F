from _010_add_new_donor import call_get_donor_inputs
from _010_add_new_donor import write_donor_data_in_file
from _020_add_new_event import call_get_event_inputs
from _020_add_new_event import print_donation_successful
from _020_add_new_event import write_event_data_in_file
from _030_delete_donor import delete_donor_data_from_file
from _040_delete_event import delete_event_data_from_file
from _050_list_data import list_donor_data, list_event_data
import time
import os

ACTIONS = ("1", "2", "3", "4", "5", "6", "7")


def menu():
	os.system("CLS")
	print("-" * 71)
	print("--- Welcome to the coolest donor and donation event managing system ---")
	print("-" * 71)
	print("""
Main menu

	1. Add new donor
	2. Add new donation event
	3. Delete donor
	4. Delete donation event
	5. List donors or donation events
	6. Search
	7. Exit
	""")
	action = input("Please choose your action: ")
	while action not in ACTIONS:
		print("To exit press 7, otherwise enter a number from 1 to 6.")
		action = input("Please choose your action:  ")
	if action == "1":
		os.system("CLS")
		call_get_donor_inputs()
		time.sleep(3)
		os.system("CLS")
		write_donor_data_in_file()
		time.sleep(3)
		os.system("CLS")
		menu()
	if action == "2":
		os.system("CLS")
		call_get_event_inputs()
		time.sleep(3)
		os.system("CLS")
		print_donation_successful()
		time.sleep(3)
		os.system("CLS")
		write_event_data_in_file()
		time.sleep(3)
		os.system("CLS")
		menu()
	if action == "3":
		os.system("CLS")
		delete_donor_data_from_file()
		menu()
	if action == "4":
		os.system("CLS")
		delete_donor_data_from_file()
		menu()
	if action == "5":
		os.system("CLS")
		choice = input("Donor (1) or event (2) ?: ")
		if choice == "1":
			list_donor_data()
			main_menu = input("Back to the main menu? (y): ")
			while main_menu != "y":
				main_menu = input("Back to the main menu? (y): ")
				menu()
		if choice == "2":
			list_event_data()
			main_menu = input("Back to the main menu? (y): ")
			while main_menu != "y":
				main_menu = input("Back to the main menu? (y): ")
				menu()
	# if action == "6":
	if action == "7":
		exit()

if __name__ == '__main__':
	menu()
