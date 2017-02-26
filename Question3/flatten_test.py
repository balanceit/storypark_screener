# flatten_test.py

import unittest
from flatten import flatten

class FlattenTest(unittest.TestCase):
	""" Testing of the flatten method """

	def test_flatten_simple(self):
		self.assertEquals([1], flatten([1]))
		self.assertEquals([1,2,3,4], flatten([1,2,3,4]))

	def test_flatten_empty(self):
		self.assertEquals([], flatten([]))

	def test_flatten_nested(self):
		expected = [1,2,3,4]
		make_flat = [[1,2,[3]],4]
		self.assertEquals(expected, flatten(make_flat))

	def test_flatten_deep_nested(self):
		expected = [1,2,3,4,5,6]
		make_flat = [1,2,[3,[4,[5,[6]]]]]
		self.assertEquals(expected, flatten(make_flat))

	def test_flatten_mixed_with_empty(self):
		expected = [1,2,3,4,5,6,7,8,9,10,11,12,13]
		make_flat = [1,[2,[],[],[[[[]]]],[3,[4,[5,[6],7],8,[],[9],10]],11,[12],[],[[[[[[[[13]]]]]]]]]]
		self.assertEquals(expected, flatten(make_flat))


if __name__ == '__main__':
    unittest.main()