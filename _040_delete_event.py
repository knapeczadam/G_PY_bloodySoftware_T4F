import csv


def delete_event_data_from_file():

    data = []

    with open("Data\events.csv") as csvfile_read:
        csvreader = csv.reader(csvfile_read, delimiter=",")
        for row in csvreader:
            if row:
                data.append(row)
    csvfile_read.close()
    with open("Data\events.csv", "r") as donors_csv:
        read_donors_csv = csv.reader(donors_csv)
        print("Existing IDs: \n")
        for row in read_donors_csv:
            if len(row) > 0:
                print("\t" + row[0])
    dicta = {}
    x = 1
    for elements in data:
        dicta[x] = elements
        x += 1
    delete = input("Enter an ID what u want to delete: ")
    if delete:
        for k in dicta:
            if delete in dicta[k]:
                print(dicta[k])
                dicta.pop(k)
                break
                
    #IDE MEG KELL VELEMI HOGY VISSZA TERJEN A MAIN BA

    with (open("Data\events.csv", 'w')) as writer:
        csvwriter = csv.writer(writer, delimiter=",")
        for word in dicta:
            csvwriter.writerow(dicta[word])
