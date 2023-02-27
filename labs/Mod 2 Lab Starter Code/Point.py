class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_from_origin(self):
        return (self.x**2 + self.y**2)**(1/2)

    def __lt__(self, p2):
        if self.dist_from_origin() < p2.dist_from_origin():
            return True
        else:
            return False

    def __eq__(self, p2):
        if (self.x == p2.x) and (self.y == p2.y):
            return True
        else:
            return False
    
    def __gt__(self, p2):
        if self.dist_from_origin() > p2.dist_from_origin():
            return True
        else:
            return False

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)

if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(1, 2)
    p3 = Point(1, 2)
    p4 = Point(4, 3)
    p5 = Point(10, 8)
    p6 = Point(0, 0)

    assert p1.x == 3
    assert p1.y == 4

    print(p1.dist_from_origin())
    print(p6.dist_from_origin())

    #print(p1 > p4) problem when distance is equal
    print(p2 < p4)
    print(p4 < p2)

    print(p2 == p3)
    print(p2 == p4)

    print(p5 > p1)
    print(p1 > p5)

    s = str(p1)
    print(s)
    t = str(p5)
    print(t)
