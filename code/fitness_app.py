# Test driven development 
# Write tests before writing code
# TDD has 3 phases:
#	Red - Write a test, run your code. It fails.
#	Green - Modify your code until it passes
#	Refactor - Clean up your code: keep it D.R.Y

#Let's write a fitness app! We want to keep track of the following:
#	Runs - Each run should track:
#		time
#		distance
#		calories burned
#		
#	Strength - Each strength activity should track:
#		time
#		reps
#		weight
#		calories burned

class Activity:
	def __init__(self, time, calories):
		self.time = time
		self.calories = calories

class Run(Activity):
	def __init__(self, time, distance, calories):
		super().__init__(time, calories)
		self.distance = distance

class Strength(Activity):
	def __init__(self, time, reps, weight, calories):
		super().__init__(time, calories)
		self.reps = reps
		self.weight = weight

#r1 = Run(25, 2, 200)
#assert(r1.time == 25)
#assert r1.distance == 2 # parentheses are not required
#assert r1.calories == 200
#print("tests passed!")

#s1 = Strength(2, 10, 25, 50)
#assert s1.time == 2
#assert s1.reps == 10
#assert s1.weight == 25
#assert s1.calories == 50
#print("tests passed!")
