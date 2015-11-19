from donor_inputs import DonorInputHelper
from datetime import datetime
from Data import donors


class AddNewDonor:

    data = []

    with open("donor.csv") as csvfile_read:
        csvreader = donors.reader(csvfile_read, delimiter=",")
        for row in csvreader:
            if row:
                data.append(row)
    csvfile_read.close()
    dicta = {}
    x = 1
    for elements in data:
        dicta[x] = elements
        x += 1
    print(dicta)

    delete = input("Would you like to pop an item?")
    if delete:
        if delete.isdigit:
            dicta.pop(int(delete))

    main_do_name = DonorInputHelper.get_name()
    main_do_gender = DonorInputHelper.get_gender()

    main_do_weight = DonorInputHelper.get_weight()      # If the returned number from the
    if int(main_do_weight) <= 50:                       # def is not greater than 50, the program stops.
        print("\nDonors are only accepted above 50 kgs.")
        print("The program has ended because of not suitable donor.")
        exit()

    # If the returned date from the def is within 18 years of the current date, the program stops.
    main_do_birth = DonorInputHelper.get_date_of_birth()

    if (datetime.now() - datetime.strptime(main_do_birth, "%Y.%m.%d")).days // 365 < 18:
        print("\nDonors are only accepted above 18 years.")
        print("The program has ended because of not suitable donor.")
        exit()

    # If the returned date from the def is within 90 days of the current date, the program stops.
    main_do_last_don = DonorInputHelper.get_donation_date()
    if (datetime.now() - datetime.strptime(main_do_last_don, "%Y.%m.%d")).days <= 90:
        print("\nDonors can only give blood once in every 3 months.")
        print("The program has ended because of not suitable donor.")
        exit()
    main_do_sick = DonorInputHelper.get_sickness()

    if main_do_sick.lower() == "y":
        print("-----")
        print("The program has ended because of not suitable donor.")
        exit()
    main_do_id = DonorInputHelper.get_id_number()
    #elobb vagy utan

    main_do_exp_id = DonorInputHelper.get_exp_date()
    if datetime.strptime(main_do_exp_id, "%Y.%m.%d") < datetime.now():
        print("Expired! Program is shutting down...")
        exit()
    main_do_blood = DonorInputHelper.get_blood_type()
    main_do_email = DonorInputHelper.get_email_address()
    main_do_mobile = DonorInputHelper.get_mobile_number()
    print("The donor's data is recorded.")
    Donor_data = [main_do_name, main_do_gender, main_do_weight, main_do_birth, main_do_last_don, main_do_sick, main_do_id, main_do_exp_id, main_do_blood, main_do_email, main_do_mobile]
    print(Donor_data)

    data = []

    with open("donor.csv") as csvfile_read:
        csvreader = donors.reader(csvfile_read, delimiter=",")
        for row in csvreader:
            if row:
                data.append(row)
    csvfile_read.close()

    dicta = {}
    x = 1
    for elements in data:
        dicta[x] = elements
        x += 1
    print(dicta)

    delete = input("Would you like to pop an item?")
    if delete:
        if delete.isdigit:
            dicta.pop(int(delete))

    print(dicta)
    with (open("donor.csv", 'w')) as writer:
        csvwriter = donors.writer(writer, delimiter=",")
        for word in dicta:
            csvwriter.writerow(dicta[word])

    with open("donor.csv", "a") as csvfile_write:
        csvwriter = donors.writer(csvfile_write, delimiter=',')
        csvwriter.writerow(Donor_data)
        print("New:", Donor_data)

    z = input("Do you want to clear the donor data from? (Y/N)")
    if z.lower() == "y":
        open("donor.csv", 'w').close()
        print("Cleared!")
