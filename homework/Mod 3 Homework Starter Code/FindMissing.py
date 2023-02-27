import random

def find_missing_1(L):
    n = len(L) + 1
    for i in range(n):
        if i in L:
            continue
        else:
            return i

def find_missing_2(L):
    L = sorted(L)
    for i in range(1, len(L)):
        if L[0] != 0:
            return 0
        elif L[len(L) - 1] != len(L):
            return len(L)
        elif (L[i] - L[i-1] == 1):
            continue
        else:
            return L[i] - 1

def find_missing_3(L):
    a = len(L) * (len(L) + 1) / 2
    b = sum(L)
    return int(a - b)

def find_missing_4(L):
    S = set(L)
    n = len(S) + 1
    for i in range(n + 1):
        if i in S:
            continue
        else:
            return i

if __name__ == '__main__':
    # Create a randomized permutation with one element missing
    N = 5
    my_list = list(range(N + 1))
    random.seed()
    random.shuffle(my_list)
    my_list.pop()

    # Print the output
    print(find_missing_1(my_list))
    print(find_missing_2(my_list))
    print(find_missing_3(my_list))
    print(find_missing_4(my_list))
