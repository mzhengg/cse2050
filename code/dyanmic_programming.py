def dyn_fc(amt, coins):
    solved = {i:i for i in range(1, amt+1)} # "optimal solutions" assuming pennies

    for a in range(1, amt+1):
        for c in coins:
            if c == a:
                solved[a] = 1
                break
            elif c < a:
                n = 1 + solved[a-c]
                if n < solved[a]:
                    solved[a] = n
    return solved[amt]

coins = [1, 5, 10, 21, 25]
assert dyn_fc(50, coins) == 2