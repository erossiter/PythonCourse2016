import unittest
from ordinalLab import *

class ordinalTest(unittest.TestCase):
	
	def test_output(self):
		self.assertEqual('1st', ordinalFunc(1))
		self.assertEqual('2nd', ordinalFunc(2))
		self.assertEqual('3rd', ordinalFunc(3))
		self.assertEqual('4th', ordinalFunc(4))
		
		self.assertNotEqual('1rd', ordinalFunc(1))
		self.assertNotEqual('10st', ordinalFunc(10))
		self.assertNotEqual('2th', ordinalFunc(2))
		self.assertNotEqual('3', ordinalFunc(3))
	
	def test_input(self):
		ar = ["a", "b"]
		self.assertEqual("Input must be integer", ordinalFunc("a"))
		self.assertEqual("Input must be integer", ordinalFunc(1.5))
		self.assertEqual("Input must be integer", ordinalFunc(ar))
  
if __name__ == '__main__': #Add this if you want to run the test with this script.
  unittest.main()
