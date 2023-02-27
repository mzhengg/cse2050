import math as m

class Vector:
    def __init__(self):
        raise NotImplementedError

    def __add__(self, vector):
        try:
            x = self.get_x() + vector.get_x()
            y = self.get_y() + vector.get_y()
            if isinstance(self, RecVec):
                return RecVec(x, y)
            else:
                if x != 0:
                    return PolVec(round((x**2 + y**2)**(1/2), 2), round(m.degrees(m.atan(y/x)), 2))
                else:
                    return False
        except:
            raise TypeError

    def __sub__(self, vector):
        try:
            x = self.get_x() - vector.get_x()
            y = self.get_y() - vector.get_y()
            if isinstance(self, RecVec):
                return RecVec(x, y)
            else:
                if x != 0:
                    return PolVec(round((x**2 + y**2)**(1/2), 2), round(m.degrees(m.atan(y/x)), 2))
                else:
                    return False
        except:
            raise TypeError
        
    def __eq__(self, vector):
        try:
            x1 = self.get_x()
            x2 = vector.get_x()
            y1 = self.get_y()
            y2 = vector.get_y()

            if (x1 == x2) and (y1 == y2):
                return True
            else:
                return False
        except:
            raise TypeError

    def rectangular(self):
        return RecVec(self.get_x(), self.get_y())

    def polar(self):
        return PolVec(self.get_mag(), self.get_ang())

class RecVec(Vector):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "RecVec(x = {}, y = {})".format(self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_mag(self):
        return round((self.x**2 + self.y**2)**(1/2), 2)

    def get_ang(self):
        return round(m.degrees(m.atan(self.y/self.x)), 2)

class PolVec(Vector):
    def __init__(self, mag, ang):
        self.x = mag
        self.y = ang

    def __str__(self):
        return "PolVec(mag = {}, angle = {})".format(self.x, self.y)

    def get_x(self):
        return round(self.x * m.cos(m.radians(self.y)), 2)

    def get_y(self):
        return round(self.x * m.sin(m.radians(self.y)), 2)

    def get_mag(self):
        return self.x

    def get_ang(self):
        return self.y