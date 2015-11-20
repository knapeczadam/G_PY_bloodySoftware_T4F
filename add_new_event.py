from event_inputs import EventInputHelper
import csv




class AddNewEvent:
	def write_event_data_infile():
		main_ev_date_of_event = EventInputHelper.get_date_of_event()
		main_ev_start_time = EventInputHelper.get_start_time()
		main_ev_end_time = EventInputHelper.get_end_time()
		main_ev_zip_code = EventInputHelper.get_zip_code()
		main_ev_city = EventInputHelper.get_city()
		main_ev_address = EventInputHelper.get_address()
		main_ev_beds = EventInputHelper.get_available_beds()
		main_ev_don_num = EventInputHelper.calc_max_donor_number()
		main_ev_plan_don_num = EventInputHelper.get_planned_donor_number()
		main_ev_succ_don = EventInputHelper.get_succesfull_donations()


		if float(main_ev_succ_don) / float(main_ev_plan_don_num) < 0.2:
			print("Unsuccessful, not worth to organise there again")

		if 0.2 <= float(main_ev_succ_don) / float(main_ev_plan_don_num) <= 0.75:
			print("Normal event")

		if 0.75 <= float(main_ev_succ_don) / float(main_ev_plan_don_num) <= 1.1:
			print("Successful")

		if float(main_ev_succ_don) / float(main_ev_plan_don_num) > 1.1:
			print("Outstanding")
		data = []

		with open("Data\events.csv") as csvfile_read:
			csvreader = csv.reader(csvfile_read, delimiter=",")
			for row in csvreader:
				if row:
					data.append(row)
		csvfile_read.close()

		dicta = {}
		x = 1
		for elements in data:
			dicta[x] = elements
			x += 1

		Event_data = [main_ev_date_of_event, main_ev_start_time, main_ev_end_time, main_ev_zip_code, main_ev_city, main_ev_address, main_ev_beds, main_ev_don_num, main_ev_plan_don_num, main_ev_succ_don]

		print("The event's data has been recorded.")
		# ujra beleirja az eddigi adatokat.. mert yolo
		with (open("Data\events.csv", 'w')) as writer:
			csvwriter = csv.writer(writer, delimiter=",")
			for word in dicta:
				csvwriter.writerow(dicta[word])
		# a legujjabat a veg�re irja ki
		with open("Data\events.csv", "a") as csvfile_write:
			csvwriter = csv.writer(csvfile_write, delimiter=',')
			csvwriter.writerow(Event_data)
			print("New event:", Event_data)

