import random
from matplotlib import pyplot as plt
from FindMissing import find_missing_1, find_missing_2, find_missing_3, find_missing_4
from TimeFunctions import time_function

x1 = [i for i in range(0, 1001, 50)]
x2 = [i for i in range(0, 1000001, 50000)]

y1 = []
for n in x1:
    y1_average = []
    for c in range(5):
        L = [i for i in range(n + 1)]
        random.seed()
        random.shuffle(L)
        L.pop()
        y1_average.append(1000*time_function(find_missing_1, L))
    y1.append(sum(y1_average)/len(y1_average))

y2_x1 = []
for n in x1:
    y2_average = []
    for c in range(5):
        L = [i for i in range(n + 1)]
        random.seed()
        random.shuffle(L)
        L.pop()
        y2_average.append(1000*time_function(find_missing_2, L))
    y2_x1.append(sum(y2_average)/len(y2_average))

y2_x2 = []
for n in x2:
    y2_average = []
    for c in range(5):
        L = [i for i in range(n + 1)]
        random.seed()
        random.shuffle(L)
        L.pop()
        y2_average.append(1000*time_function(find_missing_2, L))
    y2_x2.append(sum(y2_average)/len(y2_average))

y3 = []
for n in x2:
    y3_average = []
    for c in range(5):
        L = [i for i in range(n + 1)]
        random.seed()
        random.shuffle(L)
        L.pop()
        y3_average.append(1000*time_function(find_missing_3, L))
    y3.append(sum(y3_average)/len(y3_average))

y4 = []
for n in x2:
    y4_average = []
    for c in range(5):
        L = [i for i in range(n + 1)]
        random.seed()
        random.shuffle(L)
        L.pop()
        y4_average.append(1000*time_function(find_missing_4, L))
    y4.append(sum(y4_average)/len(y4_average))

plt.figure()
plt.scatter(x1, y1, c='r', marker='o', label='find_missing_1')
plt.xlabel('number of items * 1')
plt.ylabel('running time (ms)')
plt.legend()
#plt.show()
plt.savefig('find_missing_1.png')

plt.figure()
plt.scatter(x1, y1, c='r', marker='o', label='find_missing_1')
plt.scatter(x1, y2_x1, c='b', marker='x', label='find_missing_2')
plt.xlabel('number of items * 1')
plt.ylabel('running time (ms)')
plt.legend()
#plt.show()
plt.savefig('find_missing_12.png')

x2 = [i/1000000 for i in range(0, 1000001, 50000)]

plt.figure()
plt.scatter(x2, y2_x2, c='y', marker='o', label='find_missing_2')
plt.scatter(x2, y3, c='g', marker='*', label='find_missing_3')
plt.xlabel('number of items * 1000000')
plt.ylabel('running time (ms)')
plt.legend()
#plt.show()
plt.savefig('find_missing_23.png')

plt.figure()
plt.scatter(x2, y3, c='m', marker='o', label='find_missing_3')
plt.scatter(x2, y4, c='k', marker='s', label='find_missing_4')
plt.xlabel('number of items * 1000000')
plt.ylabel('running time (ms)')
plt.legend()
#plt.show()
plt.savefig('find_missing_34.png')