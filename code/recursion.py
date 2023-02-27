def recr_fact(n):
    if n != 0:
        return n*recr_fact(n-1)
    else:
        return 1

x = recr_fact(4)

def greedy_fc(amt, coins):
    coins.sort(reverse=True)

    n = 0
    for c in coins:
        while c <= amt:
            amt -= c
            n += 1

    return n

def naive_recr(amt, coins):
    n_opt = amt # assume we have pennies
    
    for c in coins:
        if c == amt: 
            return 1

        elif c < amt:
            n = naive_recr(amt-c, coins) + 1

            if n < n_opt: # update "optimal solution" if appropriate
                n_opt = n

    return n_opt

def fewest_coins(amt, coins):
    if amt in coins: return 1

    valid_coins = [c in coins if c < amt]

    min_coins = amt
    
    for coins in valid_coins:
        num_coins = 1 + fewest_coins(amt-coin, coins)

        if num_coins < min_coins: min_coins = num_coins
    
    return min_coins

def helper(amt, coins):
    solved = dict()
    return memo_recr(amt, coins, solved)

def memo_recr(amt, coins, solved):
    if amt in solved: return solved[atm]

    solved[amt] = amt # initialize optimal sol. with pennies

    for c in coins:
        if c == amt:
            solved[amt] = 1
            return 1
        elif c < amt:
            n = memo_recr(amt-c, coins, solved) + 1

            if n < solved[amt]:
                solved[amt] = n

    return solved[amt]

if __name__ == '__main__':
    coins = [1, 5, 10, 25]
    assert greedy_fc(50, coins) == 2
    assert greedy_fc(28, coins) == 4
    print("all done!")

    coins = [1, 21, 25]
    #assert greedy_fc(63, coins) == 3

    coins = [1, 10, 25]
    assert naive_recr(50, coins) == 2
    assert naive_recr(27, coins) == 3

    coins = [1, 21, 25]
    assert naive_recr(63, coins) == 3

    print("all done!")
