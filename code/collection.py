# list: built in collection type that is
#		* mutuable - we can change items
#		* sequential - we can index items by their position

l = ["a", "b", "c", "d"]
print(l[2])

l[2] = "hello"
print(l[2])

print()
for item in l:
	print(item)

#      0   1     2     3       4
l = ["a", 3, 3.14, True, [4,5,6]]
print(l[4])

my_list = [1,2,3] #mutable, sequential selection of anything
my_tuple = (4,5,6) #immutable, sequential collection of anything
my_string = "abc" #immutable, sequential collection of characters
my_set = {7,8,9} #mutable, non-sequential collection of immutable objects (strings and tuples)
my_dictionary = {1:"one",   #mutable, non-sequential collection of key-value pairs
				 2:"two",   #keys: immutable
				 3:"three"} #values: mutable

print()
collections = [my_list, my_tuple, my_string, my_set, my_dictionary]
for c in collections:
	for item in c:
		print(item)
	print()

#iterating over dictionaries
for x in my_dictionary:
	print(x) #print keys

for x in my_dictionary.values():
	print(x) #print values

for key, value in my_dictionary.items():
	print(key, value) #print keys and values
