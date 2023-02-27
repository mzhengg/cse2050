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
