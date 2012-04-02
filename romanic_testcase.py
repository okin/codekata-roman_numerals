import unittest
from converter import ArabicRomanConverter

class TestArabicToRomans(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testConcversion(self):
		arc = ArabicRomanConverter

		self.assertEqual('I', arc.convert(1))
		self.assertEqual('V', arc.convert(5))
		self.assertEqual('X', arc.convert(10))
		self.assertEqual('L', arc.convert(50))
		self.assertEqual('C', arc.convert(100))
		self.assertEqual('D', arc.convert(500))
		self.assertEqual('M', arc.convert(1000))
		self.assertEqual('IX', arc.convert(9))

	def testWrongInput(self):
		pass

	def testNegativeInput(self):
		pass

if __name__ == '__main__':
	unittest.main()
	