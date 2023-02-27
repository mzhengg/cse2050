def bs(L, item):
    # base case: L is empty
    if len(L) == 0: return False

    median = len(L) // 2

    if L[median] == item: return True

    elif L[median] < item: return bs(L[median+1:], item)
    # we already checked for the median value in line 7

    elif L[median] > item: return bs(L[:median], item)

# 64 + 32 + 16 + 8 + 4 + 2 + 1 + 0

# general case:
# n/2 + n/4 + n/8 + ... + 1 = n(1/2 + 1/4 + 1/8 + 1/16 + ... + 1/n) = n*1 = O(n)


if __name__ == '__main__':
    n = 128
    L = [i for i in range(n)]

    for i in range(n):
        assert bs(L, i)

    assert not bs(L, n)