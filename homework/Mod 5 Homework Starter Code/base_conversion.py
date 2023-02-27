# Convert a number to a given base (integer less than 10)
# Return the answer as a string
# Recursive implementation required
def convert_to_base(number, base):
    if number == 0:
        return 0
    else:
        return h_convert_to_base(number, base, "")[::-1]

def h_convert_to_base(number, base, out):
    if number < base:
        return out + str(number)
    else:
        r = number % base
        out += str(r)
        number = number // base
        return h_convert_to_base(number, base, out)

if __name__ == '__main__':
    assert(convert_to_base(593, 3) == '210222')
    assert(convert_to_base(15895, 7) == '64225')
    assert(convert_to_base(95736, 8) == '272770')
