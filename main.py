print("----------------------------------------------------------------------- \
      \n--- Welcome to the coolest donor and donation event managing system --- \
      \n-----------------------------------------------------------------------")
print("Main menu")
print("\t 1. Add new donor \
    \n \t 2. Add new donation event \
    \n \t 3. Delete donor \
    \n \t 4. Delete donation event \
    \n \t 5. List donors or donation events \
    \n \t 6. Search \
    \n \t 7. Exit")
actions = ("1", "2", "3", "4", "5", "6", "7")
action = input("Please choose your action: ")
while action not in actions:
    print("To exit press 7, otherwise enter a number from 1 to 6.")
    action = input("Please choose your action:  ")
if action == "1":
    from add_new_donor import AddNewDonor
    AddNewDonor.write_donor_data_infile()
elif action == "2":
	from add_new_event import AddNewEvent
	AddNewEvent.write_event_data_infile()
elif action == "3":
    from delete_donor import DeleteDonor
    DeleteDonor.delete_donor_data_fromfile()
elif action == "4":
    from delete_event import DeleteEvent
    DeleteEvent()
elif action == "5":
    from list_data import ListData
    ListData()
elif action == "6":
    from search_data import SearchData
    SearchData()
elif action == "7":
    exit()