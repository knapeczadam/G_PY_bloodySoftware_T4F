from _010_add_new_donor import *
from _020_add_new_event import *
from _030_040_delete import *
from _050_list_data import *
from csv_helper import *
from _060_search_data import *
from _070_modify_data import *
import time
import os

ACTIONS = ("1", "2", "3", "4", "5", "6", "7", "8")
ANSWER = ["y", "yes"]
DONOR = "Donor"
DONOR_PATH = "Data\donors.csv"
DONORS_ID = 7
DONOR_ROW = 4
EVENT = "Event"
EVENTS_PATH = "Data\events.csv"
EVENTS_ID = 0
EVENT_ROW = 3


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
	5. List
	6. Search
	7. Modify
	8. Exit
	""")
	action = input("Please choose your action: ")
	while action not in ACTIONS:
		print("To exit press 8, otherwise enter a number from 1 to 7.")
		action = input("Please choose your action:  ")
	if action == "1":
		sleep_and_clean()
		if_csv_is_not_exist(DONOR_PATH)
		call_get_donor_inputs()
		print_after_writing()
		check_first_row_and_write(DONOR_PATH, donor_data_in_file(), donor_first_row())
	if action == "2":
		sleep_and_clean()
		if_csv_is_not_exist(EVENTS_PATH)
		call_get_event_inputs()
		sleep_and_clean()
		print_donation_successful()
		sleep_and_clean()
		check_first_row_and_write(EVENTS_PATH, event_data_in_file(), event_first_row())
	if action == "3":
		sleep_and_clean()
		if_csv_is_not_exist(DONOR_PATH)
		delete_data_from_file(DONOR_PATH, DONORS_ID, check_if_file_is_empty(DONOR_PATH), donor_first_row())
		sleep_and_clean()
	if action == "4":
		sleep_and_clean()
		if_csv_is_not_exist(EVENTS_PATH)
		delete_data_from_file(EVENTS_PATH, EVENTS_ID, check_if_file_is_empty(EVENTS_PATH), event_first_row())
		sleep_and_clean()
	if action == "5":
		sleep_and_clean()
		print("List:\n\t1. Donors\n\t2. Events\n\t0. Return to the Main menu")
		choice = input("\nPlease choose your action: ")
		while choice not in ["1", "2", "0"]:
			choice = input("Please choose your action: ")
		if choice == "1":
			sleep_and_clean()
			if_csv_is_not_exist(DONOR_PATH)
			check_if_file_is_empty(DONOR_PATH)
			print("Sorted by:")
			for name in donor_first_row():
				print("\t", name)
			answer = input("which?: ")
			if answer == "":
				list_donor_data(check_if_file_is_empty(DONOR_PATH), 1)
				back_to_the_main_menu()
			while answer not in donor_first_row():
				answer = input("which?: ")
			for index, element in enumerate(donor_first_row()):
				if answer == element:
					list_donor_data(check_if_file_is_empty(DONOR_PATH), index)
			back_to_the_main_menu()
		if choice == "2":
			sleep_and_clean()
			if_csv_is_not_exist(EVENTS_PATH)
			check_if_file_is_empty(EVENTS_PATH)
			print("Sorted by:")
			for name in event_first_row():
				print("\t", name)
			answer = input("Which?: ")
			if answer == "":
				list_event_data(check_if_file_is_empty(EVENTS_PATH), 1)
				back_to_the_main_menu()
			while answer not in event_first_row():
				answer = input("which?: ")
			for index, element in enumerate(event_first_row()):
				if answer == element:
					list_event_data(check_if_file_is_empty(EVENTS_PATH), index)
			back_to_the_main_menu()
	if action == "6":
		sleep_and_clean()
		print("Search in:\n\t1. Donors\n\t2. Events\n\t0. Return to the Main menu")
		choice = input("\nPlease choose your action: ")
		while choice not in ["1", "2", "0"]:
			choice = input("\nPlease choose your action: ")
		if choice.upper() == "1":
			sleep_and_clean()
			if_csv_is_not_exist(DONOR_PATH)
			search_data(check_if_file_is_empty(DONOR_PATH), DONOR, DONOR_ROW)
			back_to_the_main_menu()
		if choice.upper() == "2":
			sleep_and_clean()
			if_csv_is_not_exist(EVENTS_PATH)
			search_data(check_if_file_is_empty(EVENTS_PATH), EVENT, EVENT_ROW)
			back_to_the_main_menu()
	if action == "7":
		sleep_and_clean()
		print("Modify:\n\t1. Donors\n\t2. Events\n\t0. Return to the Main menu")
		choice = input("\nPlease choose your action: ")
		while choice not in ["1", "2", "0"]:
			choice = input("\nPlease choose your action: ")
		if choice.upper() == "1":
			sleep_and_clean()
			if_csv_is_not_exist(DONOR_PATH)
			modify_data(check_if_file_is_empty(DONOR_PATH), DONORS_ID, DONOR_PATH, donor_first_row(), DONOR)
			back_to_the_main_menu()
		if choice.upper() == "2":
			sleep_and_clean()
			if_csv_is_not_exist(EVENTS_PATH)
			# modify_events(check_if_file_is_empty(EVENTS_PATH))
			back_to_the_main_menu()
	if action == "8":
		print("Bye!")
		# os.system("CLS")
		sleep_and_clean()
		exit()
	menu()


def back_to_the_main_menu():
	"""

	:return:
	"""
	user_answer = input("\nBack to the main menu? (y or yes): ")
	while user_answer.lower() != "y":
		user_answer = input("Back to the main menu? (y or yes): ")
	menu()


def sleep_and_clean():
	"""

	:return:
	"""
	time.sleep(2)
	os.system("CLS")

if __name__ == '__main__':
	menu()
