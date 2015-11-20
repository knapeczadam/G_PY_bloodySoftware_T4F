import csv # JELENLEG CSAK KEY SZERINT VAGY TELJESEN TOROL , AZ ID-N MEG GONDOLKOZOM
class DeleteDonor:
    def delete_donor_data_fromfile():

        data = []

        with open("Data\donors.csv") as csvfile_read:
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
        print(dicta)

        delete = input("Would you like to delete an item?")
        if delete:
            if delete.isdigit:
                dicta.pop(int(delete))
            else:
                pass

        print(dicta)
        with (open("Data\donors.csv", 'w')) as writer:
            csvwriter = csv.writer(writer, delimiter=",")
            for word in dicta:
                csvwriter.writerow(dicta[word])

        z = input("Do you want to clear the donors data file? (Y/N)")
        if z.lower() == "y":
            open("Data\donors.csv", 'w').close()
            print("The donors data file has been cleared!")
