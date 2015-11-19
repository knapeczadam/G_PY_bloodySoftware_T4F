from datetime import timedelta
from datetime import datetime
from donor import DonorValidator

PREPARATION_TIME = 30
DONATION_TIME = 30


# VALIDATOR CLASS
class EventValidator:
    # Date validation imported from donor.py, call it as DonorValidator.is_valid_date()


    def valid_donation_start(date):
        if datetime.strptime(date, "%H:%M"):
            return True
        else:
            print("Incorrect format. Try again.")
            return False

    def valid_date_of_event(date_text):
        if datetime.datetime.strptime(date_text, '%Y-%m-%d'):
            return True
        else:
            print("Incorrect data format, should be YYYY-MM-DD")
            return False


    def is_valid_time(TIME):
        try:
            datetime.strptime(TIME, "%H:%M")
            return True
        except:
            return False

    def is_valid_zip_code(ZIP):
        if str(ZIP).isdigit() and len(ZIP) == 4:
            if ZIP[0] != "0":
                return True
            else:
                print(ZIP, "is not vaild! 1. number must not be 0!")
                return False
        else:
            print("ZIP must be 4 DIGITS!")
            return False

    def is_valid_city(city):
        cities = ["Miskolc", "Sarospatak", "Szerencs", "Kazincbarcika"]
        if city in cities:
            return True
        return False

    def is_valid_address(address):
        if 0 < len(address) <= 25:
            return True
        return False

    def is_valid_available_beds():
        return True

    def is_valid_planned_don_num():
        return True


# INPUT HELPER CLASS
class EventInputHelper:

    def date_of_event():
        date_of_event = input("Enter your event date:")
        while EventValidator.valid_date_of_event(date_text) is False:
            print("Is NOT a valid date of event")
        return date_of_event

    def donation_start():
        donation_start = input("Enter the start of the donation:")
        while EventValidator.valid_donation_start(date_text) is False:
            print("Is NOT a valid time.")
        return donation_start

    def get_date_of_event():
        return date_of_event

    def get_start_time():
        return start_time

    def get_end_time():
        end_time = input("Enter your donation end:")
        while EventValidator.is_valid_time(end_time) is False:
            print("Is NOT a vaild TIME")
        return end_time

    def get_zip_code():
        zip_code = input("Enter your zip:")
        while EventValidator.is_valid_zip_code(zip_code) is False:
            print("You no ZIP")
        return zip_code

    def get_city():
        city = input("Please type in where will the event take place; Miskolc, Sarospatak, Szerencs or Kazincbarcika: ")
        while EventValidator.is_valid_city(city) is False:
            print("Wrong format. Try again...")
            city = input("Please type in where will the event take place; Miskolc, Sarospatak, Szerencs or Kazincbarcika: ")
        return city

    def get_address():
        address = input("Please enter in what address will the event take place: ")
        while EventValidator.is_valid_address(address) is False:
            print("Wrong format. The address can be 25 characters long at most. Try again...")
            address = input("Please enter in what address will the event take place: ")
        return address

    def get_available_beds():
        return available_beds

    def get_planned_don_num():
        return planned_don_num