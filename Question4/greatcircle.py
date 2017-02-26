# greatcircle.ph

"""
A simple module to assist in the calculation of distances along a sphere.

See https://en.wikipedia.org/wiki/Great-circle_distance for more information
"""

import math

class Point:
	"""
	The Point class which is ment to represent a point on a sphere
	"""

	def __init__(self, latitude, longitude):
		"""
		Initialises a Point class

		Raises an AssertionError when

			- `latitude` or `longitude` is not an int or a float type
			- `latitude` is greater than 90 or less than -90
			- `longitude` is greater than 180 or less than -180
		"""

		assert type(latitude) == int or type(latitude) == float, "latitude must be a number"
		assert type(longitude) == int or type(longitude) == float, "longitude must be a number"

		assert latitude <= 90.0 and latitude >= -90.0, "latitude must between -90 and +90 (inclusive)"
		assert longitude <= 180.0 and longitude >= -180.0, "longitude must between -180 and +180 (inclusive)"

		self.latitude = float(latitude)
		self.longitude = float(longitude)

	def distance_to(self, point, radius=(6371.0 * 1000.0)):
		"""
			Returns the great circle distance, in meters, (orthodromic distance) between `self` and `point`.

			`point`: a Point instance

			`radius`: the radius of the sphere, in meters, along which to calculate the distance, defaults to the
					Earth's radius of 6,371,000.0 meters

			Raises an AssertionError when `point` is not of type Point
		"""

		assert type(point) == type(self), "the point argument must of of type Point(lat, long)"
		distance = 0.0

		# convert to radians
		phi_1 = math.radians(self.latitude);
		phi_2 = math.radians(point.latitude);

		delta_theta = math.radians(point.longitude - self.longitude)

		# calculate the delta sigma, the central angle between `self` and `point`
		delta_sigma = math.acos(math.sin(phi_1) * math.sin(phi_2) + math.cos(phi_1) * math.cos(phi_2) * math.cos(delta_theta))

		return radius * delta_sigma


