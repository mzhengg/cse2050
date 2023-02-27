def is_sorted(L): 
    for i in range(len(L) - 1):
        if L[i] > L[i+1]: return False
    return True

def selection_sort(L):
    # Find next biggest item
    # Swap that item to the correct spot

    for j in range(len(L) - 1):
        biggest_index = 0
        for i in range(1, len(L) - j): # we already have 0 as the initial biggest index, so redundancy removed
            if L[i] > L[biggest_index]: biggest_index = i

        L[biggest_index], L[len(L)-1-j] = L[len(L)-1-j], L[biggest_index]


if __name__ == '__main__':
    import random
    L = [random.randint(0, 10) for i in range(1000)]
    L.append(-1)

    assert(not is_sorted(L))
    selection_sort(L)
    assert(is_sorted(L))