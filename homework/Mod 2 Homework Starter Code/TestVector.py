import unittest
from Vector import Vector, RecVec, PolVec

class TestVector(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(NotImplementedError):
            v1 = Vector()

    def test_add_sub_eq(self):
        r1 = RecVec(3, 4)
        p1 = PolVec(10, 60)

        vs = [r1, p1]

        for v in vs:
            try:
                v == 3
            except:
                pass

            try:
                3 == v
            except:
                pass

            try:
                v + 3
            except:
                pass

            try:
                3 + v
            except:
                pass
                
            try:
                v - 3
            except:
                pass

            try:
                3 - v
            except:
                pass

class TestRecVec(unittest.TestCase):
    def test_init(self):
        r1 = RecVec(1, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)

    def test_str(self):
        r1 = RecVec(1, 2)
        self.assertEqual(str(r1), "RecVec(x = 1, y = 2)")

    def test_get_x(self):
        r1 = RecVec(1, 2)
        self.assertEqual(r1.get_x(), 1)

    def test_get_y(self):
        r1 = RecVec(1, 2)
        self.assertEqual(r1.get_y(), 2)

    def test_get_mag(self):
        r1 = RecVec(1, 2)
        self.assertEqual(r1.get_mag(), 2.24)

    def test_get_ang(self):
        r1 = RecVec(1, 2)
        self.assertEqual(r1.get_ang(), 63.43)

    def test_add(self):
        r1 = RecVec(1, 2)
        p1 = PolVec(5, 30)

        r2 = r1 + p1

        isinstance((r1 + r1), RecVec)
        isinstance((r1 + p1), RecVec)
        isinstance((p1 + r1), PolVec)

        self.assertEqual(r2.get_x(), 5.33)
        self.assertEqual(r2.get_y(), 4.5)

    def test_sub(self):
        r1 = RecVec(1, 2)
        p1 = PolVec(5, 30)

        r2 = r1 - p1

        isinstance((r1 - r1), RecVec)
        isinstance((r1 - p1), RecVec)
        isinstance((p1 - r1), PolVec)

        self.assertEqual(r2.get_x(), -3.33)
        self.assertEqual(r2.get_y(), -0.5)

    def test_eq(self):
        r1 = RecVec(1, 2)
        r2 = RecVec(2, 1)
        r3 = RecVec(1, 2)

        self.assertEqual(r1, r3)
        self.assertNotEqual(r1, r2)

        r4 = RecVec(3, 4)

        self.assertNotEqual(r4, RecVec(1, 1))
        self.assertEqual(r4, RecVec(3, 4))

    def test_rectangular(self):
        p1 = PolVec(5, 30)
        r1 = p1.rectangular()

        isinstance(r1, RecVec)

    def test_polar(self):
        r1 = RecVec(1, 2)
        p1 = r1.polar()

        isinstance(p1, PolVec)

class TestPolVec(unittest.TestCase):
    def test_init(self):
        p1 = PolVec(5, 30)
        self.assertEqual(p1.x, 5)
        self.assertEqual(p1.y, 30)

    def test_str(self):
        p1 = PolVec(5, 30)
        self.assertEqual(str(p1), "PolVec(mag = 5, angle = 30)")

    def test_get_x(self):
        p1 = PolVec(5, 30)
        self.assertEqual(p1.get_x(), 4.33)

    def test_get_y(self):
        p1 = PolVec(5, 30)
        self.assertEqual(p1.get_y(), 2.5)

    def test_get_mag(self):
        p1 = PolVec(5, 30)
        self.assertEqual(p1.get_mag(), 5)

    def test_get_ang(self):
        p1 = PolVec(5, 30)
        self.assertEqual(p1.get_ang(), 30)

    def test_add(self):
        r1 = RecVec(1, 2)
        p1 = PolVec(5, 30)

        p2 = p1 + r1

        isinstance((r1 + p1), RecVec)
        isinstance((p1 + r1), PolVec)
        isinstance((p1 + p2), PolVec)

        self.assertEqual(p2.get_x(), 5.33)
        self.assertEqual(p2.get_y(), 4.5)

    def test_sub(self):
        r1 = RecVec(1, 2)
        p1 = PolVec(5, 30)

        p2 = p1 - r1

        isinstance((r1 - p1), RecVec)
        isinstance((p1 - r1), PolVec)
        isinstance((p1 - p2), PolVec)

        self.assertEqual(p2.get_x(), 3.33)
        self.assertEqual(p2.get_y(), 0.5)

    def test_eq(self):
        p1 = PolVec(1, 2)
        p2 = PolVec(2, 1)
        p3 = PolVec(1, 2)

        self.assertEqual(p1, p3)
        self.assertNotEqual(p1, p2)

        p4 = PolVec(10, 60)

        self.assertNotEqual(p4, PolVec(1, 1))
        self.assertEqual(p4, PolVec(10, 60))

    def test_rectangular(self):
        p1 = PolVec(5, 30)
        r1 = p1.rectangular()

        isinstance(r1, RecVec)

    def test_polar(self):
        r1 = RecVec(1, 2)
        p1 = r1.polar()

        isinstance(p1, PolVec)

unittest.main()