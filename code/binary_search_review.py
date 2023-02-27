def b_search_1(L, item):
    if len(L) == 1:
        return L[0] == item
    middle = len(L) // 2
    if L[middle] == item:
        return True
    if L[middle] > item:
        return b_search_1(L[:middle], item)
    if L[middle] < item:
        return b_search_1(L[middle+1:], item)

L = [i for i in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert b_search_1(sorted(L), 9)
assert not b_search_1(sorted(L), 10)

def b_search_2(L, item):
    start = 0
    end = len(L) - 1

    while (end-start) > 1:
        temp_middle = (end-start) // 2
        middle = start + temp_middle
        if L[middle] == item:
            return True
        if L[middle] > item:
            start = start
            end = middle 
        if L[middle] < item:
            start = middle
            end = end
    return L[start] == item or L[end] == item

L = [i for i in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert b_search_2(sorted(L), 0)
assert not b_search_1(sorted(L), 10)
