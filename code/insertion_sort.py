def is_sorted(L): 
    for i in range(len(L) - 1):
        if L[i] > L[i+1]: return False
    return True

def insertion_sort(L):
    n = len(L)
    for j in range(n): # Sort of an inversion of bubble sort. We are doing the last one, last two, three, and so forth.
        for i in range(n - 1 - j, n - 1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
            else:
                 break

if __name__ == '__main__':
    import random
    L = [random.randint(0, 10) for i in range(1000)]
    L.append(-1)

    assert(not is_sorted(L))
    insertion_sort(L)
    assert(is_sorted(L))