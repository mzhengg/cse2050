method = 3

print("method = {}".format(method))

if method == 1:
	import math # get access to all of math's attributes in the scope math.*

	x = math.sqrt(4)

	print("math.sqrt(4) = {}".format(x))

elif method == 2:
	from math import sqrt, pi #adds just math.sqrt() and math.pi to local scope

	x = sqrt(4)
	print("sqrt(4) = {}".format(x))
	print("pi = {}".format(pi))

elif method == 3:
	from math import * #imports all of math's attributes to local scope

	x = sqrt(4)
	print("sqrt(4) = {}".format(sqrt(x)))
	print("pi = {}".format(pi))
	print("cos(1) = {}".format(cos(1)))

	#THIS IS VERY DANGEROUS because modules have a lot of attributes and function names are reused

	print("dir() = {}".format(dir()))

elif method == 4:
	import math as m # RECOMMENDED: m can be any variable, it is the alias for math

	x = m.sqrt(4)
	print("sqrt(4) = {}".format(m.sqrt(x)))
	print("pi = {}".format(m.pi))
	print("cos(1) = {}".format(m.cos(1)))
