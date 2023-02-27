class Stack:
	def __init__(self):
		self.l = []

	def push(self, item):
		self.l.append(item)

	def pop(self, item):
		self.pop(item)

	# to make iterable, def __iter__
	# __iter__ should return an iterator

	def __iter__(self):
		return StackIterator(self)

class StackIterator:
	def __init__(self, s):
		self.s = s
		self.counter = len(self.s.l) - 1

	def __next__(self):
		# Find the next item to return
		# decrement the counter
		# return the next item
		while self.counter >= 0:
			next_item = self.s.l[self.counter]
			self.counter -= 1 
			return next_item

		# eventually, raise StopIteration error
		raise StopIteration

if __name__ == '__main__':
	s = Stack()
	for i in range(3):
		s.push(i)

	for item in s:
		print("outer = {}".format(item))
		for j in s:
			print("inner = {}".format(j))
		print()