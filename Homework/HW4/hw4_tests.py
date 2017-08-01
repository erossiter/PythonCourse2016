import unittest
from random import shuffle
from hw4_functions import *

class hw4_tests(unittest.TestCase):
	
	def test_insertionSort(self):
		a = [4, 3, 2, 1]
		b = [1]
		c = range(100)
		shuffle(c)
		d = []
		self.assertEqual([1,2,3,4], insertion_sort(a))
		self.assertEqual(b, insertion_sort(b))
		self.assertEqual(range(100), insertion_sort(c))
		with self.assertRaises(emptyListException): 
			insertion_sort(d)

	def test_mergeSort(self):
		a = [4, 3, 2, 1]
		b = [1]
		c = range(100)
		shuffle(c)
		d = []
		self.assertEqual([1,2,3,4], merge_sort(a))
		self.assertEqual(b, merge_sort(b))
		self.assertEqual(range(100), merge_sort(c))
		with self.assertRaises(emptyListException): 
			merge_sort(d)

if __name__ == '__main__':
  unittest.main()

