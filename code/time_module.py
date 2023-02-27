import time

def time_func(f, args):
    start = time.time()
    f(args)
    end = time.time()
    return end - start #this tells you how much time to run the function