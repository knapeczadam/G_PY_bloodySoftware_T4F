from datetime import timedelta
from datetime import datetime
from donor import DonorValidator

PREPARATION_TIME = 30
DONATION_TIME = 30


# VALIDATOR CLASS
class EventValidator:
	# Date validation imported from donor.py, call it as DonorValidator.is_valid_date()

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

	def is_valid_available_beds(beds):
		isvalid = str(beds).isdigit()
		if not isvalid:
			print("Please enter only numbers!")
		return isvalid

	def is_valid_planned_donor_number(number):
		return str(number).isdigit() and int(number) <= max_donor_number

	def is_valid_success_rate(number):
		return str(number).isdigit()


# INPUT HELPER CLASS
class EventInputHelper:
    def get_date_of_event():
        date_of_event = input("Enter your event date:")
        while DonorValidator.is_valid_date(date_of_event) is False:
            print("Is NOT a valid date of event")
            date_of_event = input("Enter your event date:")
        return date_of_event

    def get_start_time():
        global start_time
        start_time = input("Enter the start of the donation:")
        while EventValidator.is_valid_time(start_time) is False:
            print("Is NOT a valid time.")
            start_time = input("Enter the start of the donation:")
        return start_time

    def get_end_time():
        global end_time
        end_time = input("Enter your donation end:")
        while EventValidator.is_valid_time(end_time) is False:
            print("Is NOT a vaild TIME")
            end_time = input("Enter your donation end:")
        return end_time

    def get_zip_code():
        zip_code = input("Enter your zip:")
        while EventValidator.is_valid_zip_code(zip_code) is False:
            print("You no ZIP")
            zip_code = input("Enter your zip:")
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
        global available_beds
        available_beds = input("Please enter the number of available beds: ")
        while EventValidator.is_valid_available_beds(available_beds) is False:
            print("Wrong format. Try again...")
            available_beds = input("Please enter the number of available beds: ")
        return available_beds

    def get_planned_donor_number():
        global planned_donor_number
        planned_donor_number = input("Please enter the planned donor number: ")
        while EventValidator.is_valid_planned_donor_number(planned_donor_number) is False:
            print("x out of {}".format(max_donor_number))
            planned_donor_number = input("Please enter the planned donor number: ")
        return planned_donor_number

    def get_succesfull_donations():
        global succesfull_donation
        succesfull_donation = input("Please enter how many successfull donations\
    were during donation event (x out of {})".format(max_donor_number))
        while EventValidator.is_valid_success_rate(succesfull_donation) is False:
            print("must be only digits")
            succesfull_donation = input("Please enter how many successfull donations\
    were during donation event (x out of {})".format(max_donor_number))
        return succesfull_donation

    def calc_max_donor_number():
        global max_donor_number
        event_duration_in_minutes = datetime.strptime(end_time, "%H:%M") \
                                    - datetime.strptime(start_time, "%H:%M")
        event_duration_in_minutes = timedelta.total_seconds(event_duration_in_minutes) // 60
        max_donor_number = ((event_duration_in_minutes - PREPARATION_TIME) \
                            // DONATION_TIME) * int(available_beds)
        return max_donor_number
