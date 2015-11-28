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
ANSWER = ["y", "yes"]


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
		sleep_and_clean()
		call_get_donor_inputs()
		sleep_and_clean()
		write_donor_data_in_file()
		sleep_and_clean()
		menu()
	if action == "2":
		sleep_and_clean()
		call_get_event_inputs()
		sleep_and_clean()
		print_donation_successful()
		sleep_and_clean()
		write_event_data_in_file()
		sleep_and_clean()
		menu()
	if action == "3":
		sleep_and_clean()
		delete_donor_data_from_file()
		sleep_and_clean()
		menu()
	if action == "4":
		sleep_and_clean()
		delete_donor_data_from_file()
		sleep_and_clean()
		menu()
	if action == "5":
		sleep_and_clean()
		choice = input("Donor (1) or event (2) ?: ")
		if choice == "1":
			list_donor_data()
			back_to_the_main_menu()
		if choice == "2":
			list_event_data()
			back_to_the_main_menu()
		while choice not in ["1", "2"]:
			choice = input("Donor (1) or event (2) ?: ")
			if choice == "1":
				list_donor_data()
				back_to_the_main_menu()
			if choice == "2":
				list_event_data()
				back_to_the_main_menu()
	# if action == "6":
	if action == "7":
		# os.system("CLS")
		print("Bye!")
		sleep_and_clean()
		exit()


def back_to_the_main_menu():
	"""

	:return:
	"""
	user_answer = input("Back to the main menu? (y or yes): ")
	while user_answer.lower() != "y":
		user_answer = input("Back to the main menu? (y or yes): ")
	menu()


def sleep_and_clean():
	"""

	:return:
	"""
	# time.sleep(2)
	os.system("CLS")

if __name__ == '__main__':
	menu()
