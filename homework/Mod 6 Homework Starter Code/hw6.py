def is_sorted(L):
    return not any(L[i] > L[i+1] for i in range(len(L)-1))

def bubble_sort(L):
    n = len(L)
    for j in range(n-1):
        for i in range(n-1-j):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]

def champaign_sort(L):
    n = len(L)
    for i in range(n-1):
        swaps = 0
        for j in range(n-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                swaps += 1
        for k in range(n-2-i, 0, -1):
            if L[k] < L[k-1]:
                L[k], L[k-1] = L[k-1], L[k]
                swaps += 1
        if swaps == 0:
            break

def insertion_sort(L):
    n = len(L)
    for j in range(n-1):
        i = n-1-j
        while i < n and L[i] < L[i-1]:
            L[i], L[i-1] = L[i-1], L[i]
            i += 1

def b_search(L, start, end, item):
    left, right = start, end
    while right - left > 1:
        median = (right + left) // 2
        if item < L[median]:
            right = median
        else:
            left = median
    if item <= L[left]:
        return left
    else:
        return right

def opt_insertion_sort(L): #[1, 4, 5, 2, 3]
    n = len(L)
    end = len(L)
    for j in range(n-1):
        i = n-2-j
        start = n-1-j
        sorted_end = b_search(L, start, end, L[i])
        for k in range(i, sorted_end-1):
            if L[k] > L[k+1]:
                L[k], L[k+1] = L[k+1], L[k]

if __name__ == '__main__':
    import random
    L = [i for i in range(10)]
    random.shuffle(L)
    assert not is_sorted(L)
    bubble_sort(L)
    assert is_sorted(L)
    
    L = [i for i in range(10)]
    random.shuffle(L)
    assert not is_sorted(L)
    champaign_sort(L)
    assert is_sorted(L)

    L = [i for i in range(10)]
    random.shuffle(L)
    assert not is_sorted(L)
    insertion_sort(L)
    assert is_sorted(L)

    L = [i for i in range(10)]
    random.shuffle(L)
    assert not is_sorted(L)
    opt_insertion_sort(L)
    assert is_sorted(L)

