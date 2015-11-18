from datetime import timedelta
from datetime import datetime
from donor import DonorValidator

PREPARATION_TIME = 30
DONATION_TIME = 30


# VALIDATOR CLASS
class EventValidator:
    # Date validation imported from donor.py, call it as DonorValidator.is_valid_date()

    def is_valid_time():
        return True

    def is_valid_zip_code():
        return True

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
    def get_date_of_event():
        return date_of_event

    def get_start_time():
        return start_time

    def get_end_time():
        return end_time

    def get_zip_code():
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