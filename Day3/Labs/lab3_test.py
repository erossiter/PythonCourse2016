import unittest
from lab3 import *

class labTests(unittest.TestCase):
	
	def test_shout(self):
		self.assertEqual("HELLO!", shout("hello"))
		self.assertNotEqual("Hello!", shout("hello"))
		with self.assertRaises(stringException): shout(5)
		
	def test_reverse(self):
		self.assertEqual("olleh", reverse("hello"))

	def test_reversewords(self):
		self.assertEqual("there Hello", reversewords("Hello there"))
		with self.assertRaises(multipleWordException): reversewords("hello")
		
 	def test_reversewordletters(self):
 		self.assertEqual("olleh ereht", reversewordletters("hello there"))
 		self.assertEqual("olleh", reversewordletters("hello"))

 	def test_piglatin(self):
 		self.assertEqual("erina", piglatin("erin"))
 		self.assertEqual("obba", piglatin("bob"))
 		self.assertEqual("erina anda obba", piglatin("erin and bob"))
 		self.assertNotEqual("joe", piglatin("joe"))

if __name__ == '__main__':
  unittest.main()

