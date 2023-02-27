def is_sorted(L):
    return not(any(L[i] > L[i+1] for i in range(len(L)-1)))

def bubble(L):
    n = len(L)
    # scan list from left ro right
    # if items are out of place, swap them

    for i in range(n): # after n-1 passes: the n-1 biggest items are in their final place and the smallest item has to be first. Thus, we can save a loop.
        for j in range(n-1-i): # the -i is so that every success run of the inner for-loop ensures that we dont sort the last i biggest items again.
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j] # this holds the values in temporary variables before fully commiting

            # after one pass, the biggest item is in the last slot
            # after two passes, the two biggest items are in the last slots


def selection(L): # different from bubble in that we are not doing many intermidate swaps with every loop, we are finding the largest then doing one final swap
    n = len(L)

    for i in range(n-1):
        # find the biggest item
        biggest = 0 # this is an index not a value
        for j in range(1, n-i): # skip 0 because biggest is already at index 0. Also, -i ensures we dont sort the last i items for each successive inner for loop again
            if L[j] > L[biggest]: # finds the index of the biggest value in the list
                biggest = j
        # move it to the end
        L[biggest], L[j] = L[j], L[biggest] # note, j takes on the value that was last assigned to it by the for loop: n-1
        # L[biggest]: location of the largest item
        # L[j]: location of the last iterated j in the for loop, which will always be the last item before the sorted ones
        # =
        # L[j] = value of that last iterated j in the for loop
        # L[biggest] = value of the largest item
        # Here, biggest equals the j where the value was largest it is not equal to the j displayed here, that j is above^^^

def insertion(L):
    n = len(L)

    for i in range(n-1):
        item = L[n-2-i] # Second to last item: We dont look at the last item because it is always sorted relative to itself
        j = n-1-i # Last item

        while j < n and L[j] < item:
            L[j-1] = L[j]
            j += 1

        L[j-1] = item

if __name__ == '__main__':
    assert is_sorted([1, 2, 3,])
    assert not is_sorted([1, 2, 1])
    print("all passed!")


    import random
    n = 100
    L = [random.randint(0, 100) for i in range(n)]
    L.append(-1)
    assert not(is_sorted(L))
    bubble(L)
    assert is_sorted(L)

    n = 100
    L = [random.randint(0, 100) for i in range(n)]
    L.append(-1)
    assert not(is_sorted(L))
    selection(L)
    assert is_sorted(L)

    n = 100
    L = [random.randint(0, 100) for i in range(n)]
    L.append(-1)
    assert not(is_sorted(L))
    insertion(L)
    assert is_sorted(L)