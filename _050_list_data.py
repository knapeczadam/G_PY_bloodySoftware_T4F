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
		print("\n%s." % key, end=" ")
		for element in dicta[key]:
			if element == dicta[key][0]\
					or element == dicta[key][2]\
					or element == dicta[key][3]\
					or element == dicta[key][9]:
				print("\t %s" % element)


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

	for key in dicta:
		print("\n%s." % key, end=" ")
		for element in dicta[key]:
				print("\t%s" % element)
