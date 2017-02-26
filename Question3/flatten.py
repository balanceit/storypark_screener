# main.py
def flatten(int_list):
	"""
		Assuming `int_list`is a list of arbitrarily nested lists of integer values
		this will return a "flatten" list of those values in the original order
		ignoring any empty lists
	"""
	flat_list = []
	for i in int_list:
		if isinstance(i, list):
			flat_list.extend(flatten(i))
		else:
			flat_list.append(i)
	return flat_list
