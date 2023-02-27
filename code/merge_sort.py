def is_sorted(L):
    return not any(L[i] > L[i+1] for i in range(len(L)-1))

def merge_sort(L):
    # 1) Divide into subproblems
    # 2) Solve our subproblems
    # 3) Combine sub-solutions into main solution

    # Base case: list with 1 or fewer items
    if len(L) <= 1: return L

    # Breaks lists into left and right sub-lists
    median = len(L) // 2
    left = L[:median]
    right = L[median:]

    # Recursively split up the sub-lists into even smaller sub-lists until base case is reached
    left = merge_sort(left)
    right = merge_sort(right)

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i+j] = left[i]
            i += 1
        else:
            L[i+j] = right[j]
            j += 1
    # Note, i and j have a 1 added after adding the item to the sub-list at this level of recursion so the i and j below will be one item after
    L[i+j:] = left[i:] + right[j:]

    # Return list to next level of recursion in the corresponding left and right recursive calls
    return L

import random
L = [random.randint(0,10) for i in range(1000)]
L.append(-1)

assert not is_sorted(L)
merge_sort(L)
assert is_sorted(L)