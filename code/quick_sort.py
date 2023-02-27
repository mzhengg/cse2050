def is_sorted(L):
    return not any(L[i] > L[i+1] for i in range(len(L) - 1))

def quick_sort(L, left = 0, right = None):
    if right is None: right = len(L)

    if (right - left) <= 1: return None

    # Partition around a pivot

    pivot = right - 1 # always picking last item as pivot
    i, j = left, right - 2 # i is first item and j is last item that is not pivot (second to last)

    # Pivot:
    while i < j: # we are incrementing i to the right and j to the left until they overlap
        # Find first item bigger than pivot
        while L[i] < L[pivot]: # i will necessarily terminate as in the worst case it reaches the pivot itself and becomes equal to it
            i += 1
        # i leaves off at the index of the value that is greater than or equal to the pivot
        while L[j] >= L[pivot] and i < j: # j will not necessarily terminate because it lies below the pivot, thus another base conditional required
            j -= 1
        # j leaves off at the index of the value that is less than the pivot
        if i < j: # swap those i and j
            L[i], L[j] = L[j], L[i]

    # eventually, when the while loop breaks, i and j will overlap on the first element of the right half and at the point is where the pivot best splits the list in half
    if L[i] >= L[pivot]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    # by now, the pivot will be in the middle, roughly splitting the left and right in half
    quick_sort(L, left, pivot) # recursively call on left half
    quick_sort(L, pivot+1, right) # recursively call on right half 

import random
n = 10
L = [random.randint(0, n) for i in range(n)]
L.append(-1)

assert not is_sorted(L)
quick_sort(L)
assert is_sorted(L)