def find_missing_2(L):
    L.sort()
    if L[0] != 0:
        return 0
    elif L[len(L) - 1] != len(L):
        return len(L)
    else:
        for i in range(1, len(L)):
            if (L[i] - L[i-1] == 1):
                continue
            else:
                return L[i] - 1