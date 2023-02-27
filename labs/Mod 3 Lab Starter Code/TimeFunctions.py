import time

def time_function(func, args):
    pass
    # get current time from computer
    start = time.time()
    # run function
    func(args)
    # return difference between current time and start time
    end = time.time()
    return end - start

if __name__ == '__main__':
    def test_func(L):
        for item in L:
            item *= 2

    L1 = [i for i in range(10**5)]
    t1 = time_function(test_func, L1)

    L2 = [i for i in range(10**6)]
    t2 = time_function(test_func, L2)

    # L2 contains 10x more items than L1, so we expect it to take 10x as long to run.
    print("t(L1) = {:.3g} ms".format(t1*1000))
    print("t(L2) = {:.3g} ms".format(t2*1000))
    # Note how time is converted to ms to make things prettier.
    # "prettiness" is CRUCIAL when presenting data: make it as easy as possible for others to understand what you do.