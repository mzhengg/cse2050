import sys
def compute_mean(the_list):
    if len(the_list) > 0:
        sum_num = 0
        for item in the_list:
            sum_num = sum_num + item
        return float(sum_num / len(the_list))
    else:
        return float(0)
        
def compute_median(the_list):
    sorted_list = sorted(the_list)
    if (len(sorted_list)%2) == 0:
        return float(sorted_list[int((len(sorted_list)/2)-1)])
    else:
        return float(sorted_list[int(len(sorted_list)//2)])

def compute_mode(the_list):
    sorted_list = sorted(the_list)
    num_dict = {}
    for item in sorted_list:
        if item in num_dict.keys():
            num_dict[item] = num_dict[item] + 1
        else:
            num_dict[item] = 1
    max_freq = 1
    mode = sorted_list[0]
    for key, value in num_dict.items():
        if value > max_freq:
            max_freq = value
            mode = key
        else:
            pass
    return float(mode)

if __name__ == '__main__':
    numbers = []
    for line in sys.stdin:     # iterate over input line by line
        for n in line.split(): # split the line at standard whitespace characters
            if n == 'done':
                break
            else:
                try:
                    numbers.append(int(n))  # add character groups to the list "numbers"
                except ValueError:
                    pass

    # TODO: figure out a way to exit the for loop when a user enters "done"

    # TODO: implement the functions above, then print their results as follows
    print(compute_mean(numbers))
    print(compute_median(numbers))
    print(compute_mode(numbers))