# main.ph
"""
	Using a file `staff_list.json` which is assumed to exist in this same directory, output an
	array of dicts containing staff members names and their distances from `office_point`.

	This output will be sorted (assesnding) by the staff members name and only contain staff members
	distance from the Storypark home office `office_point` is less than 2000 meters (`within_meters`).

	It is assumed that the `staff_list.json` file has a `staff` key at it's root which is an array
	of objects which are assumed to have the structure of:

		{
			'name': the name of the staff member,
			'location': {
				'latitude': the latitude of this staff members location,
				'longitude': the longitude of this staff members location
			}
		}

"""

import math
import json
import pprint
from greatcircle import Point

# define the location of the Storypark offices
office_point = Point(-41.2920728, 174.7748162)

# read in the json file
with open('staff_list.json') as data_file:
	data = json.load(data_file)
    
# get all the staff
staff = data["staff"]

# this will hold all staff who are within the distance defined in `within_meters`
close_staff = []
within_meters = 2000.0

for s in staff:
	lat = s["location"]["latitute"]
	lon = s["location"]["longitude"]
	p = Point(lat,lon)

	# find the great circle distance and append the the `close_staff` list
	# if within the defined distance
	distance_meters = office_point.distance_to(p)
	if distance_meters < within_meters:
		close_staff.append( { 'name': s["name"], 'distance': distance_meters } )

# sort `close_staff` by name
close_staff.sort( key=lambda o: o["name"] )

print ''
print 'All staff within', within_meters, ' meters'
pp = pprint.PrettyPrinter()
pp.pprint(close_staff)
print ''