def find_min(L, m=1):
    start = 0
    end = len(L)-1

    while end-start > 1:
        temp_middle = (((end-start) + 1) // 2)
        middle = start + temp_middle
        if L[middle] > L[middle-m]:
            start = start
            end = middle
        if L[middle-m] > L[middle]:
            start = middle
            end = end

    return min(L[start], L[end])

if __name__ == "__main__":
    assert find_min([5,2,2,2,1,3,4,8], 1) == 1
    assert find_min([20,19,17,13,10,9,6,3,1,0], 1) == 0
    assert find_min([0,1,2,3,4,5,6,7,8,9], 1) == 0
    assert find_min([10,9,6,3,1,0,2,4,5,8], 1) == 0