def bs(L, item, left=0, right=None):
     if right is None: right = len(L) - 1

     median = (left + right) // 2

     if L[median] == item: return True
     
     if (right - left) <= 1: return L[right] == item

     if L[median] > item: return bs(L, item, left, median)
     elif L[median] < item: return bs(L, item, median, right)

if __name__ == '__main__':
    n = 128
    L = [i for i in range(n)]

    for i in range(n):
        assert bs(L, i)

    assert not bs(L, n)
    assert not bs(L, -1)