# 1 import unittest
# 2 import classes to tet
# 3 defne a new class for every class you want to test
#   these must inherit from the class unittest.Testcase
# 4 create one method per test case
# 5 run unittest.main()

import unittest
from fitness_app import Activity, Run, Strength

class TestRun(unittest.TestCase):
	def test_init(self):
		r1 = Run(25, 2, 200)
		self.assertEqual(r1.time, 25)
		self.assertEqual(r1.distance, 2)
		self.assertEqual(r1.calories, 200)

class TestStrength(unittest.TestCase):
	def test_init(self):
		s1 = Strength(2, 10, 25, 50)
		self.assertEqual(s1.time, 2)
		self.assertEqual(s1.reps, 10)
		self.assertEqual(s1.weight, 25)
		self.assertEqual(s1.calories, 50)

unittest.main()