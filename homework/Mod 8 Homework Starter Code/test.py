from TempMap import *
tm = TempMap()
p1 = (36.4482, -105.0072)
p2 = (36.44, -105.00) # rounds to the same as p1
tm.add_report(p1, 25)
# before removal - get works
assert tm[p1] == (25, 25)
tm.remove_pos(p1)
# after removal - get raises keyError
try:
    tm[p1]
    raise AssertionError
except KeyError:
    pass
# cannot remove twice
try:
    tm.remove_pos(p1)
    raise AssertionError
except KeyError:
    pass