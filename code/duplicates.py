def dup_1(L):
    n = len(L) # 1
    for i in range(n): # 2x
        for j in range(n): # 2x
            if i != j and L[i] == L[j]: # 2x
                return True # 1
    return False

# 1 + n * n * 2 + 1 = 2n^2 + 2

def dup_2(L):
    n = len(L) # 1
    return any(L[i] == L[j] for i in range(1, n) for j in range(i))

# (n^2)/2 - n/2 + 2

