from week3_lecture import time_trials
from matplotlib import pyplot as plt

def sum_iter(k):
    s = 0
    for i in range(1, k+1):
        s += i
    return s

def sum_mul(k):
    return (k/2) * (k+1)

# is adding a list o a list an atomic function?
def add_lists(L1, L2):
    return L1 + L2

if __name__ == '__main__':
    assert sum_iter(0) == 0
    assert sum_iter(1) == 1
    assert sum_iter(4) == 10

    assert sum_mul(0) == 0
    assert sum_mul(1) == 1
    assert sum_mul(4) == 10

# print table header
print("="*34)
print("{:>10}  {:10}  {:10}".format("n", "t_iter", "t_mul"))
print("-"*34)

# print table lines
ns = [100*i for i in range(10)]
for n in ns:
    t_iter = time_trials(sum_iter, [n])
    t_mul = time_trials(sum_mul, [n])
    print("{:>10}  {:<10.3}  {:<10.3}".format(n, t_iter, t_mul))
 #  print("{:>10}  {:<10.3f}  {:<10.3g}".format(n, t_iter, t_mul)) # f forces a float, g forces which ever is prettier
 #  print("{:>10}  {:<10.3e}  {:<10.3}".format(n, t_iter, t_mul)) # e forces exponential, default is float

# print table footer
ns = [1000*i for i in range(10)]
t_iter = []
t_mul = []
t_lists = []

for n in ns:
    L1 = [i for i in range(n)]
    L2 = [i for i in range(n)]
    Ls = [L1, L2]
    t_iter.append(1E6*time_trials(sum_iter, [n], 100))
    t_mul.append(1E6*time_trials(sum_mul, [n], 100))
    t_lists.append(1E6*time_trials(add_lists, Ls, 100))

plt.scatter(ns, t_iter, label="iter")
plt.scatter(ns, t_mul, label="mul")
plt.scatter(ns, t_lists, label="lists")
plt.xlabel("No. of items")
plt.ylabel("time (microseconds)")
plt.legend()
plt.show()