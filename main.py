# Main menu options come here shortly - by calling classes from the freshly separated files.

Event_data = []

# Welcomes to the program and starts an option.
print("Welcome to the blood donation program.\n")
d_e_s = ""
d_e_s_list = ["D", "E", "S", "d", "e", "s"]
# Keeps asking the user which program option to run till one of the above listed letters is chosen.
while d_e_s not in d_e_s_list:
    d_e_s = input("To start a Donor registration press D; \
                    \nTo start an Event registration press E; \
                    \nTo Stop the program press S: ")

# DONOR REGISTRATION
# In case D is entered, calls all the Donor definitions.
if d_e_s.upper() == "D":    # add_new_donor.py function calls will be here
    pass

# EVENT REGISTRATION
# In case E is entered, calls all the Event definitions.
elif d_e_s.upper() == "E":  # add_new_event.py function calls will be here
    pass

# In case S is entered, the program stops.
elif d_e_s.upper() == "S":
    print("The program ended normally.")
    exit()

