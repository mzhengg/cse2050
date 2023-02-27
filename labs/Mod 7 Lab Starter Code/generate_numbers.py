# This program generates a list of numbers and writes them to a file.
import random

##### Generate list of numbers #####
n = 10000                                       # number of ints to generate
L = [random.randint(0, n) for i in range(n)]    # list of random ints
 
##### Create file to write to #####
f = open(f"unsorted_{n}.txt", "w")  # create new file in write mode

##### Write numbers to file #####
for item in L:
    f.write(str(item))
    f.write(" ")

#### Close the file ####
f.close()