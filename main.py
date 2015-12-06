from os import system
from time import sleep
from msvcrt import getch
from _030_040_delete import *
from _050_list_data import *
from _060_search_data import *
from _070_modify_data import *
from csv_helper import *

ANSWER = ["y", "yes"]
LIST = "List"
SEARCH = "Search"
MODIFY = "Modify"

DONOR_STRING = "Donor"
DONOR_PATH = "Data\donors.csv"
DONOR_ID_INDEX_IN_ROW = 7
PAGES_DURING_D_LIST_SEARCH = 4
donor_header = lambda: donor_first_row()
donors_csv = lambda: pure_data_from_csv_file(DONOR_PATH)

EVENT_STRING = "Event"
EVENT_PATH = "Data\events.csv"
EVENT_ID_INDEX_IN_ROW = 0
PAGES_DURING_E_LIST_SEARCH = 3
event_header = lambda: event_first_row()
events_csv = lambda: pure_data_from_csv_file(EVENT_PATH)

HOW_MANY_HYPHENS_IN_A_ROW = 71  # Ctrl+ Alt + V
clear = lambda: system('CLS')

ALL_ACTION = {
	'KEY_ONE': 49,
	'KEY_TWO': 50,
	'KEY_THREE': 51,
	'KEY_FOUR': 52,
	'KEY_FIVE': 53,
	'KEY_SIX': 54,
	'KEY_SEVEN': 55,
	'KEY_ESC': 27
}


def menu():
	loading()
	if_csv_is_not_exist(DONOR_PATH)
	check_first_row_and_write(DONOR_PATH, donor_header())
	if_csv_is_not_exist(EVENT_PATH)
	check_first_row_and_write(EVENT_PATH, event_header())
	render_menu()
	do_action()
	menu()


def render_menu():
	print("-" * HOW_MANY_HYPHENS_IN_A_ROW)
	print("--- Welcome to the coolest donor and donation event managing system ---")
	print("-" * HOW_MANY_HYPHENS_IN_A_ROW)
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


def do_action():
	action = ord(getch())
	while action not in list(ALL_ACTION.values()):
		action = ord(getch())
	if action == ALL_ACTION['KEY_ONE']:
		clear(), add_new_donor()
	if action == ALL_ACTION['KEY_TWO']:
		clear(), add_new_event()
	if action == ALL_ACTION['KEY_THREE']:
		clear(), delete_donor()
	if action == ALL_ACTION['KEY_FOUR']:
		clear(), delete_event()
	if action == ALL_ACTION['KEY_FIVE']:
		clear(), submenu(LIST)
	if action == ALL_ACTION['KEY_SIX']:
		clear(), submenu(SEARCH)
	if action == ALL_ACTION['KEY_SEVEN']:
		clear(), submenu(MODIFY)
	if action == ALL_ACTION['KEY_ESC']:
		print("Bye!"), exit()


def submenu(string_name_of_submenu):
	print(
		"{} (press 1, 2 or ESC):\n\t1. Donor\n\t2. Event\n\tEsc. Back to the Main menu".format(string_name_of_submenu))
	action = ord(getch())
	while action not in list(ALL_ACTION.values()):
		action = ord(getch())
	if action == ALL_ACTION['KEY_ONE']:
		if not file_is_empty(DONOR_PATH):
			loading()
			if LIST == string_name_of_submenu:
				list_donor()
			if SEARCH == string_name_of_submenu:
				search_donor()
			if MODIFY == string_name_of_submenu:
				modofy_donor()
	if action == ALL_ACTION['KEY_TWO']:
		if not file_is_empty(EVENT_PATH):
			loading()
			if LIST == string_name_of_submenu:
				list_events()
			if SEARCH == string_name_of_submenu:
				search_event()
			if MODIFY == string_name_of_submenu:
				modify_event()
	if action == ALL_ACTION['KEY_ESC']:
		menu()


def add_new_donor():
	if call_donor_get_functions():
		print_suitable_donor_data()
		new_donor_data = new_donor_to_list()
		append_new_donor_or_event_to_csv(DONOR_PATH, new_donor_data)


def add_new_event():
	if call_event_get_functions():
		print_donation_successful()
		new_event_data = new_event_to_list()
		append_new_donor_or_event_to_csv(EVENT_PATH, new_event_data)


def delete_donor():
	if not file_is_empty(DONOR_PATH):
		delete_data_from_file(DONOR_PATH, DONOR_ID_INDEX_IN_ROW, donors_csv(), donor_header(), DONOR_STRING)


def delete_event():
	if not file_is_empty(EVENT_PATH):
		delete_data_from_file(EVENT_PATH, EVENT_ID_INDEX_IN_ROW, events_csv(), event_header(), EVENT_STRING)


def list_donor():
	print("Sorted by:")
	for number, header_name in zip(range(1, 14), donor_header()):
		print("\t", number, header_name)
	answer = input("which number?: ")
	while answer not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '']:
		answer = input("which number?: ")
	if answer == '':
		answer = 2  # sorted by last name index
	list_donor_data(donors_csv(), int(answer) - 1, PAGES_DURING_D_LIST_SEARCH)


def list_events():
	print("Sorted by:")
	for number, header_name in zip(range(1, 14), event_header()):
		print("\t", number, header_name)
	answer = input("which number?: ")
	while answer not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
		answer = input("which number?: ")
	list_donor_data(events_csv(), int(answer) - 1, PAGES_DURING_E_LIST_SEARCH)


def search_donor():
	if not file_is_empty(DONOR_PATH):
		search_data(donors_csv(), DONOR_STRING, PAGES_DURING_D_LIST_SEARCH)


def search_event():
	if not file_is_empty(EVENT_PATH):
		search_data(events_csv(), EVENT_STRING, PAGES_DURING_E_LIST_SEARCH)


def modofy_donor():
	if not file_is_empty(DONOR_PATH):
		modify_data(DONOR_PATH, DONOR_ID_INDEX_IN_ROW, donors_csv(), donor_header(), DONOR_STRING)


def modify_event():
	if not file_is_empty(EVENT_PATH):
		modify_data(EVENT_PATH, EVENT_ID_INDEX_IN_ROW, events_csv(), event_header(), EVENT_STRING)


def loading():
	"""

	:return:
	"""
	system("CLS")
	x = "Loading."
	for dot in range(3):
		print(x)
		x += "."
		sleep(0.2)
	system("CLS")


if __name__ == '__main__':
	menu()
