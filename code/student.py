class Person:
	def __init__(self, name, num):
		self._name = name #leading underscore suggests "private" attribute
		self._num = num
		self._courses = []

	def name(self):
		return self._name

	def num(self):
		return self._num

	def courses(self):
		return self._courses

class Student(Person): #Inheritance: student inherits all attributes from person
	def __str__(self):
		return "Student: name = {}\tnum = {}".format(self._name, self._num) #retrieves private attributes - no no

class Professor(Person):
	def __str__(self):
		return "Professor: name = {}\tnum = {}".format(self.name(), self.num()) #retrieves attributes via getter functions - good job



s1 = Student("Rachel", 1234)
p1 = Professor("Jake", 5678)
print(s1._name) #should not access private attributes (variables) outside of the class
print(s1.name()) #correct way to access private attributes

print(s1)
print(p1)