class Vector:
	def __init__(self, x, y): #initializes every new instance of this class
		self.x = x
		self.y = y

	def magnitude(self):
		return (self.x**2 + self.y**2)**(1/2)

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)

	def __str__(self): #python, by default, prints the memory location of the vector and not the actual vector. This tells it to do the latter
		return "Vector({}, {})".format(self.x, self.y)

v = Vector(3, 4)
u = Vector(5, 6)

print("v.x = {}\tv.y = {}".format(v.x, v.y))
print("u.x = {}\tv.y = {}".format(u.x, u.y))

print("Vector.magnitude(v) = {}".format(Vector.magnitude(v)))

print("v.magnitude() = {}".format(v.magnitude()))

w = Vector.__add__(u, v)
w = u.__add__(v)
w = u + v #for every call of +, python looks for __add__
print("u.add(v) = {}".format(w))

x = 3
print(int.__add__(3,4))
print(x.__add__(4))
#print(3.__add__(4)) this does not work, 3 must first be defined as a variable with class int
