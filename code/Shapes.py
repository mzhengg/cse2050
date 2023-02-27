class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.len = x**2 

    def mag(self):
        return self.len

    def __repr__(self): # code-like string repr
        return "Point({}, {})".format(self.x, self.y)

    def __str__(self): # human readable string
        return "It's a point, yo: x = {}, y = {}".format(self.x, self.y)

class Polygon:
    def __init__(self, sides, points):
        if sides != len(points):
            raise RunTimeError("Wrong number of points!")
        self.sides = sides
        self.points = points

    def __str__(self, name, points):
        temp = name+"\n"
        for p in self.points:
            temp += "\t{}\n".format(p)
        return temp

class Square(Polygon):
    def __init__(self, points):
        super().__init__(4, points)

    def __str__(self):
        return super().__str__("Square", points)

class Triangle(Polygon):
    def __init__(self, points):
        super().__init__(3, points)

    def __str__(self):
        return super().__str__("Triangle", points)

if __name__ == '__main__':
    p1 = Point(3, 4)
    assert p1.x == 3
    assert p1.y == 4

    assert p1.mag() == 9

    assert repr(p1) == "Point(3, 4)"
    assert str(p1) == "It's a point, yo: x = 3, y = 4"

    p1 = Point(0, 0)
    p2 = Point(1, 0)
    p3 = Point(1, 1)
    p4 = Point(0, 1)

    points = [p1, p2, p3, p4]
    s1 = Square(points)

    assert s1.sides == 4
    assert s1.points == [p1, p2, p3, p4]

