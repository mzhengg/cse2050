class BSTNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None # left child
		self.right = None # right child
		self.weight = 1 # number of nodes in subtree rooted at this node

	# return the node with the matching key
	def get(self, key):
		# 3 cases:
		#	1) self.key == key: return self
		#	2) self.key > key: search left subtree
		#	3) self.key < key: search right subtree

		if self.key == key: return self

		if self.key > key:
			if self.left is not None:
				return self.left.get(key)

		if self.key < key:
			if self.right is not None:
				return self.right.get(key)

		raise KeyError("key {} is not in tree".format(key))

	# update value or add key:value pair
	def put(self, key, value):
		if self.key == key:
			self.value = value
		
		elif self.key > key:
			if self.left is not None:
				self.left.put(key, value)
			else:
				self.left = BSTNode(key, value)

		elif self.key < key:
			if self.right is not None:
				self.right.put(key, value)
			else:
				self.right = BSTNode(key, value)

		self.update_weight()

	def update_weight(self):
		left_weight = self.left.weight if self.left else 0
		right_weight = self.right.weight if self.right else 0
		self.weight = left_weight + right_weight + 1

	# There might be a more simple, less complicated way to implement this.
	# take time to understand this function

	# return the node with matching key or the next lowest key
	def floor(self, key):
		# 3 cases:
		if self.key == key: return self

		if self.key > key:
			if self.left is not None: return self.left.floor(key)
			else: return None

		if self.key < key:
			if self.right is not None:
				temp_node = self.right.floor(key)
				if temp_node is not None: return temp_node
				else: return self