import csv
class DeleteEvent:
    def delete_donor_data_fromfile():

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
        for h in dicta:
            print(h, end="")
            print(dicta[h])
        delete = input("Enter an ID what u want to delete: ")
        if delete:
            if delete.isdigit():
                dicta.pop(int(delete))

        print(dicta)
        with (open("Data\events.csv", 'w')) as writer:
            csvwriter = csv.writer(writer, delimiter=",")
            for word in dicta:
                csvwriter.writerow(dicta[word])
