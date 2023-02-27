def contains(L, item):
    n = len(L)

    for obj in L:
        if obj == item:
            return True

    return False

def contains_2(L, item):
    return any(obj == item for obj in L)

if __name__ == '__main__':
    n = 100
    L = [i for i in range(n)]

    for i in range(n):
        assert contains(L, i)

    assert not contains(L, n)