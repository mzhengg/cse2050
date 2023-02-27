def is_sorted(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

def bubble_sort(L): # Doing n-1 pair swaps
    n = len(L)
    for j in range(n-1):
        for i in range(n-1-j):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]

def selection_sort(L): # Finding the largest value and doing one swap to the end
    n = len(L)
    for j in range(n-1):
        biggest = 0
        for i in range(1, n-j):
            if L[i] > L[biggest]:
                biggest = i
        L[i], L[biggest] = L[biggest], L[i]

def insertion_sort(L): # Start from the end and progress to the beginning, each time we are bubbling within the sub-intervals
    n = len(L)
    for i in range(n-1):
        j = n-1-i # Always last index in the unsorted sub-list
        while j < n and L[j] < L[j-1]: # j-1 always the second to last index in the unsorted sub-list
            L[j], L[j-1] = L[j-1], L[j]
            j += 1
        



L = [1, 5, 3, 9, 2, 4, 7, 6, 8, 0]
assert not is_sorted(L)
bubble_sort(L)
assert is_sorted(L)

L = [1, 5, 3, 9, 2, 4, 7, 6, 8, 0]
assert not is_sorted(L)
selection_sort(L)
assert is_sorted(L)

L = [1, 5, 3, 9, 2, 4, 7, 6, 8, 0]
assert not is_sorted(L)
insertion_sort(L)
assert is_sorted(L)
