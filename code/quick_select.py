def quickselect(L, left=0, right=None): # quick select is similiar to the quick sort algorithm but its function is to find the index of the median or the optimal pivot
    if right is None: right = len(L)

    pivot = right-1
    i, j = left, pivot-1
    
    while i<j:
        while L[i] < L[pivot]: 
            i += 1

        while L[j] >= L[pivot] and i<j: 
            j -= 1

        if i < j: 
            L[i], L[j] = L[j], L[i]

    if L[i] >= L[pivot]:
        L[i], L[pivot] = L[pivot], L[i]
        pivot = i

    if pivot == len(L) // 2: return L[pivot]

    elif pivot > len(L) // 2: return quickselect(L, left, pivot)
    
    elif pivot < len(L) // 2: return quickselect(L, pivot+1, right)

    # The reason this works is because the pivot is not constant and changes with every recursive call.
    # It also follows that the list will still be sorted since it is based on the quick sort algorithm and it turns out that the pivot
    # will always eventually taken on the middle value in the list. Thus, the moment the list is sorted, the pivot will reside in the middle
    # and line 21 will return the value at that index.

if __name__ == '__main__':
    import random
    n = 1000
    L = [i for i in range(n)]
    median = L[n//2]
    random.shuffle(L)
    assert(quickselect(L) == median)