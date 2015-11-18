from datetime import timedelta
from datetime import datetime
from donor import Validator

PREPARATION_TIME = 30
DONATION_TIME = 30


# VALIDATOR CLASS
class EventDataValidator:
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

    def is_valid_success_rate(self):
        return str(self).isdigit()


# INPUT HELPER CLASS
class EventInputHelper:
    def Input():
        global Input
        Input = input("--> ")
        return Input

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

    def get_succesfull_donations():
        print("Please enter how many successfull donations were during donation event (x out of {})".format(planned_donor_number))
        while Validator.is_valid_succces_rate(EventInputHelper.Input()) is False:
            print("must be only digits")
        return Input

    def mock_get_max_donor_number():
        global max_donor_number
        event_duration_in_minutes = end_time - start_time
        event_duration_in_minutes = timedelta.total_seconds(event_duration_in_minutes) // 60
        max_donor_number = ((event_duration_in_minutes - PREPARATION_TIME) // DONATION_TIME) * int(available_beds)
        return max_donor_number
