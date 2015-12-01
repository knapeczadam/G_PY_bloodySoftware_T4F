from _datetime import datetime
def list_donor_data(listed_donor_data):
	"""

	:param data:
	:return:
	"""
	dicta = {}
	x = 1
	for elements in listed_donor_data:
		dicta[x] = elements
		x += 1

	for key in dicta:
		if key != 1:
			print("\nKey  ----> ", dicta[key][7])
			for element in dicta[key]:

				if element == dicta[key][2]:
					print("\t %skg" % element)

				if element == dicta[key][4]:
					print("\t %s" % element, end=" - ")
					year = datetime.strptime(element, "%Y.%m.%d")
					today = datetime.now()
					age = ((today - year).days//365)
					print(age, "years old")
				if element == dicta[key][10]:
					print("\t %s" % element)
					print("-" * 40)

				if element == dicta[key][0]:
					print("-" * 40)
					print("\t", element, end=", ")
				if element == dicta[key][1]:
					print(element, end="\n")



def list_event_data(listed_event_data):
	"""

	:param data:
	:return:
	"""
	dicta = {}
	x = 1
	for elements in listed_event_data:
		dicta[x] = elements
		x += 1
	names = ["Date", "Start time", "End time", "Zip code", "City", "Address", "Available beds", "Planned donors", "Max donor numbers", "Successful donations"]

	for key in dicta:
		place = 0
		for element in dicta[key]:
			if key != 1:
				if len(element) == 12:
					print("\nKey  ---->  ", element, end="\n")
					print("-" * 40)
				if len(element) != 12:
					print(names[place])
					place += 1
					print("\t%s" % element)
	print("-" * 40)