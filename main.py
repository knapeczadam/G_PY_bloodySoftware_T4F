from _010_add_new_donor import *
from _020_add_new_event import *
from _030_040_delete import *
from _050_list_data import *
from csv_helper import *
from _060_search_data import *
from _070_modify_data import *
import time
import os
from msvcrt import getch

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
	render_menu()
	action = ord(getch())
	sleep_and_clean()
	do_action(action)
	menu()


def do_action(action):
	if action == 49:  # Ctrl + Alt + M
		add_new_donor()
	elif action == 50:
		add_new_event()
	elif action == 51:
		delete_donor()
	elif action == 52:
		delete_event()
	elif action == 53:

		print("List:\n\t1. Donors\n\t2. Events\n\t0. Return to the Main menu")
		choice = ord(getch())
		if choice == 49:
			list_donor()
		if choice == 50:
			list_events()
	elif action == 54:

		print("Search in:\n\t1. Donors\n\t2. Events\n\t0. Return to the Main menu")
		choice = ord(getch())
		if choice == 49:
			search_donor()
		if choice == 50:
			search_event()
	elif action == 55:
		print("Modify:\n\t1. Donors\n\t2. Events\n\t0. Return to the Main menu")
		choice = ord(getch())
		if choice == 49:
			modofy_donor()
		if choice == 50:
			modify_event()
	elif action == 27:
		terminate()


def render_menu():
	separator_length = 71  # Ctrl+ Alt + V
	print("-" * separator_length)
	print("--- Welcome to the coolest donor and donation event managing system ---")
	print("-" * separator_length)
	print("""
Main menu
	1. Add new donor
	2. Add new donation event
	3. Delete donor
	4. Delete donation event
	5. List
	6. Search
	7. Modify
	Esc. Exit
	""")
	print("Please choose your action: ")


def terminate():
	print("Bye!")
	sleep_and_clean()
	exit()


def modify_event():
	if_csv_is_not_exist(EVENTS_PATH)
	modify_data(check_if_file_is_empty(EVENTS_PATH), EVENTS_ID, EVENTS_PATH, event_first_row(), EVENT)
	back_to_the_main_menu()


def modofy_donor():
	from _070_modify_data import modify_data
	if_csv_is_not_exist(DONOR_PATH)
	modify_data(check_if_file_is_empty(DONOR_PATH), DONORS_ID, DONOR_PATH, donor_first_row(), DONOR)
	back_to_the_main_menu()


def search_event():
	if_csv_is_not_exist(EVENTS_PATH)
	search_data(check_if_file_is_empty(EVENTS_PATH), EVENT, EVENT_ROW)
	back_to_the_main_menu()


def search_donor():
	if_csv_is_not_exist(DONOR_PATH)
	search_data(check_if_file_is_empty(DONOR_PATH), DONOR, DONOR_ROW)
	back_to_the_main_menu()


def list_events():
	if_csv_is_not_exist(EVENTS_PATH)
	check_if_file_is_empty(EVENTS_PATH)
	print("Sorted by:")
	for name in event_first_row():
		print("\t", name)
	answer = input("Which?: ")
	if answer == "":
		list_event_data(check_if_file_is_empty(EVENTS_PATH), 1)
		back_to_the_main_menu()


def list_donor():
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


def delete_event():
	if_csv_is_not_exist(EVENTS_PATH)
	delete_data_from_file(EVENTS_PATH, EVENTS_ID, check_if_file_is_empty(EVENTS_PATH), event_first_row())
	sleep_and_clean()


def delete_donor():
	if_csv_is_not_exist(DONOR_PATH)
	pure_data = check_if_file_is_empty(DONOR_PATH)
	delete_data_from_file(DONOR_PATH, DONORS_ID, pure_data, donor_first_row())
	sleep_and_clean()


def add_new_event():
	if_csv_is_not_exist(EVENTS_PATH)
	call_get_event_inputs()
	sleep_and_clean()
	print_donation_successful()
	sleep_and_clean()
	check_first_row_and_write(EVENTS_PATH, event_data_in_file(), event_first_row())


def add_new_donor():
	if_csv_is_not_exist(DONOR_PATH)
	call_get_donor_inputs()
	# print_after_writing()
	check_first_row_and_write(DONOR_PATH, donor_data_in_file(), donor_first_row())


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
	x = "Loading."
	for dot in range(3):

		print(x)
		time.sleep(0.5)
		x += "."
	os.system("CLS")

if __name__ == '__main__':
	menu()
