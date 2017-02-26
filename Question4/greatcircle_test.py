# greatcircle_test.ph
"""The tests for the greatcircle module"""

import unittest
import math
from greatcircle import Point


class PointTest(unittest.TestCase):
	""" Testing of the Point class """

	def test_init_simple(self):
		p = Point(90, 90)
		self.assertTrue(isinstance(p, Point))

	def test_init_simple_ints(self):
		p = Point(90, 90)
		self.assertTrue(isinstance(p, Point))

	def test_init_simple_floats(self):
		p = Point(9.5, 9.5)
		self.assertTrue(isinstance(p, Point))

	def test_init_simple_neg(self):
		p = Point(-90, -89.5)
		self.assertTrue(isinstance(p, Point))

	def test_init_invalid_params_empty(self):
		with self.assertRaises(TypeError):
			p = Point()

	def test_init_invalid_params_onlyone(self):
		with self.assertRaises(TypeError):
			p = Point(1)

	def test_init_invalid_params_invalidLat(self):
		with self.assertRaises(AssertionError):
			p = Point('s', 1)
		with self.assertRaises(AssertionError):
			p = Point(True, 1)
		# check the out of bounds cases
		with self.assertRaises(AssertionError):
			p = Point(91, 1)
		with self.assertRaises(AssertionError):
			p = Point(-91, 1)

	def test_init_invalid_params_invalidLong(self):
		with self.assertRaises(AssertionError):
			p = Point(1, 's')
		with self.assertRaises(AssertionError):
			p = Point(1, True)
		# check the out of bounds cases
		with self.assertRaises(AssertionError):
			p = Point(90, 181)
		with self.assertRaises(AssertionError):
			p = Point(90, -181)

	def test_distance_to_simple(self):
		p1 = Point(0,0)
		p2 = Point(90, 180)

		d = p1.distance_to(p2)
		self.assertTrue(isinstance(d, float))

	def test_distance_to_invalid_param(self):
		p1 = Point(0,0)

		with self.assertRaises(AssertionError):
			p1.distance_to(None)
		with self.assertRaises(AssertionError):
			p1.distance_to(1)

	def test_distance_to_zero(self):
		d = Point(0, 0).distance_to(Point(0, 0))
		self.assertEquals(0.0, d)

		d = Point(20, -20).distance_to(Point(20, -20))
		self.assertEquals(0.0, d)

	def test_distance_to_nonZero(self):
		p1 = Point(0, 0)
		p2 = Point(10, 10)

		d = p1.distance_to(p2)
		self.assertTrue(d > 0.0)

	def test_distance_to_180(self):
		# half the earths circumference (roughly)
		h_cir = 6371.0 * 1000.0 * math.pi
		d = Point(0, 0).distance_to(Point(0, 180))
		self.assertEquals(h_cir, d)

		d = Point(90, 0).distance_to(Point(-90, 0))
		self.assertEquals(h_cir, d)

		d = Point(45, 0).distance_to(Point(-45, 180))
		self.assertEquals(h_cir, d)

		d = Point(75, 100).distance_to(Point(-75, -80))
		self.assertEquals(h_cir, d)

	# it is know that the distance between one degree arc
	#  of the earth is about 111 km, this is just a rough
	#  test of to ensure functionality
	def test_distance_to_one_degree(self):
		d = Point(0,0).distance_to(Point(0,1))
		self.assertEquals(111000, int(d / 1000) * 1000.0)



if __name__ == '__main__':
    unittest.main()



