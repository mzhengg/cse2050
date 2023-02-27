import time
import random
from hw6 import bubble_sort, champaign_sort, insertion_sort, opt_insertion_sort

def time_func(f, L):
    start = time.time()
    f(L)
    end = time.time()
    return end - start

L = [2 for i in range(998)]
L.insert(0, 5)
L.append(-1)
print("Bubble Sort: {}".format(time_func(bubble_sort, L)))

L = [2 for i in range(998)]
L.insert(0, 5)
L.append(-1)
print("Champaign: {}".format(time_func(champaign_sort, L)))

L = [random.randint(0,10000) for i in range(10000)]
random.shuffle(L)
print("Insertion: {}".format(time_func(insertion_sort, L)))

L = [random.randint(0,10000) in range(10000)]
random.shuffle(L)
print("Opt_Insertion: {}".format(time_func(opt_insertion_sort, L)))

