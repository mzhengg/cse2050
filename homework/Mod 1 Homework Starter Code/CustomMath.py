pi = 3.14
e = 2.72

def sqrt(num):
    try:
        return num**(1/2)
    except:
        return "{} is not a number".format(num)

def floor(num):
    if isinstance(num, int):
        return "{} is the floor".format(num)
    elif isinstance(num, float):
        if num >= 0:
            return float(int(num))
        else:
            return float(int(num)-1)
    else:
        return "{} is not a number".format(num)

def ceil(num):
    if isinstance(num, int):
        return "{} is the ceil".format(num)
    elif isinstance(num, float):
        if num >= 0:
            return float(int(num) + 1)
        else:
            return float(int(num))
    else:
        return "{} is not a number".format(num)

if __name__ == '__main__':
    print("CustomMath is being executed directly")
else:
    print("CustomMath has been imported")
