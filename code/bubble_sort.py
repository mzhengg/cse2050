def is_sorted(L): 
    for i in range(len(L) - 1):
        if L[i] > L[i+1]: return False
    return True

# Invariant
#   After j loops, the j biggest items are in their final sorted positions
def bubble_sort(L):
    for j in range(len(L) - 1): # This loop ensures all the largest values are pushed to the end
        for i in range(len(L) - 1 - j): # For each cycle of this floor loop, the largest value is pushed to the end. But the 2nd, 3rd, etc. are still in limbo.
            if L[i] > L[i+1]: # The j in the range function ensures that the most recently pushed larged items are not iterated over again because we already know they are the largest.
                L[i], L[i+1] = L[i+1], L[i]

if __name__ == '__main__':
    import random
    L = [random.randint(0, 10) for i in range(1000)]
    L.append(-1)

    assert(not is_sorted(L))
    bubble_sort(L)
    assert(is_sorted(L))