from _010_add_new_donor import call_get_donor_inputs
from _010_add_new_donor import write_donor_data_in_file
from _020_add_new_event import call_get_event_inputs
from _020_add_new_event import print_donation_successful
from _020_add_new_event import write_event_data_in_file
import time
import os

ACTIONS = ("1", "2", "3", "4", "5", "6", "7")


def menu():
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
		write_donor_data_in_file()
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
	# if action == "3":
	# if action == "4":
	# if action == "5":
	# if action == "6":
	# if action == "7":
		exit()
		pass

if __name__ == '__main__':
	menu()
