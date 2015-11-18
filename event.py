from datetime import timedelta
from datetime import datetime
from donor import Validator

PREPARATION_TIME = 30
DONATION_TIME = 30


# VALIDATOR CLASS
class Validator:

    # No is_valid_date() here again, call it from donor.py

    def is_valid_time():
        return True

    def is_valid_zip_code():
        return True

    def is_valid_city():
        return True

    def is_valid_address():
        return True

    def is_valid_available_beds():
        return True

    def is_valid_planned_don_num(self):
        return True


# INPUT HELPER CLASS
class InputHelper:
    def get_date_of_event():
        return date_of_event

    def get_start_time():
        return start_time

    def get_end_time():
        return end_time

    def get_zip_code():
        return zip_code

    def get_city():
        return city

    def get_address():
        return address

    def get_available_beds():
        return available_beds

    def get_planned_don_num():
        return planned_don_num