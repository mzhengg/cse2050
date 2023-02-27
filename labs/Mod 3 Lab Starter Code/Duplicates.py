def has_duplicates_1(L):
    n = len(L)
    for i in range(n):
        for j in range(n):
            if i!= j and L[i] == L[j]:
                return True
    return False

def has_duplicates_2(L):
    n = len(L)
    for i in range(1, n):
        for j in range(i):
            if L[i] == L[j]:
                return True
    return False

if __name__ == '__main__':
    L1 = [1,2,3,4,5]
    L2 = [1,1,2,3,4,5]
    assert(not has_duplicates_2(L1))
    assert(has_duplicates_2(L2))