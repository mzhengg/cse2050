import time

def time_trials(f, f_args, n_trials = 10):
    start = time.time()
    for i in range(n_trials):
        f(*f_args) # the asterik (*) unpacks the list of arguments in f_args to be used in function
    end = time.time()
    return end - start

