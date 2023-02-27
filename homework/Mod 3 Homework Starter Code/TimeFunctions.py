import time

def time_function(func, args):
    # get current time from computer
    start = time.time()
    # run function
    func(args)
    # return difference between current time and start time
    end = time.time()
    return end - start
