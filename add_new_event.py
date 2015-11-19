from event_inputs import EventInputHelper
from Data import events


class AddNewEvent:
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
    if float(main_ev_succ_don)\
            / float(main_ev_plan_don_num) < 0.2:
        print("Unsuccessful, not worth to organise there again")
    if 0.2 <= float(main_ev_succ_don)\
            / float(main_ev_plan_don_num) <= 0.75:
        print("Normal event")
    if 0.75 <= float(main_ev_succ_don)\
            / float(main_ev_plan_don_num) <= 1.1:
        print("Successful")
    if float(main_ev_succ_don)\
            / float(main_ev_plan_don_num) > 1.1:
        print("Outstanding")
