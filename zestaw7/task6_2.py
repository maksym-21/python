import unittest
import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self) : # zwraca string "(x, y)"
        return f'({self.x}, {self.y})'

    def __repr__(self) :  # zwraca string "Point(x, y)"
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other) :  # obsługa point1 == point2
        return True if (self.x == other.x and self.y == other.y) else False

    def __ne__(self, other) : # obsługa point1 != point2
        return False if (self.x == other.x and self.y == other.y) else True

    # Punkty jako wektory 2D.
    def __add__(self, other) : # v1 + v2
        return Point(self.x + other.x,self.y + other.y)

    def __sub__(self, other) : # v1 - v2
        return Point(self.x - other.x,self.y - other.y)

    def __mul__(self, other) : # v1 * v2, iloczyn skalarny (liczba)
        return self.x * other.x + self.y * other.y

    def cross(self, other) : # v1 x v2, iloczyn wektorowy 2D (liczba)
        return self.x * other.y - self.y * other.x

    def length(self) : # długość wektora
        return math.sqrt(self.x**2 + self.y**2)

    def __hash__(self):
        return hash((self.x, self.y)) # bazujemy na tuple, immutable points

class TestPoint(unittest.TestCase) : 
    
    def test_repr(self) :
        point = Point(5,2)
        self.assertEqual(point.__repr__(),'Point(5, 2)')

        point2 = Point(-5,-2)
        self.assertEqual(point2.__repr__(),'Point(-5, -2)')

    def test_str(self) :
        point = Point(3,4)
        self.assertEqual(point.__str__(),"(3, 4)")

        point2 = Point(-3,-4)
        self.assertEqual(point2.__str__(),'(-3, -4)')

    def test_eq(self) :
        point1 = Point(0,1)
        point2 = Point(1,0)

        self.assertFalse(point1.__eq__(point2))
        self.assertFalse(point2.__eq__(point1))

        point3 = Point(3,1)
        point4 = Point(3,1)

        self.assertTrue(point3.__eq__(point4))
        self.assertTrue(point4.__eq__(point3))

    def test_ne(self) :
        point1 = Point(0,10)
        point2 = Point(10,0)

        self.assertTrue(point1.__ne__(point2))
        self.assertTrue(point2.__ne__(point1))

        point3 = Point(3,1)
        point4 = Point(3,1)

        self.assertFalse(point3.__ne__(point4))
        self.assertFalse(point4.__ne__(point3))

    def test_add(self) :
        point1 = Point(0,10)
        point2 = Point(10,0)

        self.assertEqual(point1.__add__(point2),Point(10,10))

        point3 = Point(-3,-1)

        self.assertEqual(point3.__add__(point2),Point(7,-1))
        self.assertEqual(point1.__add__(point3),Point(-3,9))

    def test_sub(self) :
        point1 = Point(0,1)
        point2 = Point(1,0)

        self.assertEqual(point1.__sub__(point2),Point(-1,1))

        point3 = Point(-3,-1)

        self.assertEqual(point3.__sub__(point2),Point(-4,-1))
        self.assertEqual(point1.__sub__(point3),Point(3,2))

    def test_mul(self) :
        point1 = Point(-1,0)
        point2 = Point(3,-1)
        point3 = Point(4,5)

        self.assertEqual(point1.__mul__(point2),-3)
        self.assertEqual(point3.__mul__(point2),7)
        self.assertEqual(point1.__mul__(point3),-4)
        self.assertNotEqual(point1.__mul__(point3),0)

    def test_cross(self) : 
        point1 = Point(-1,0)
        point2 = Point(3,-1)
        point3 = Point(4,5)

        self.assertEqual(point1.cross(point2),1)
        self.assertEqual(point3.cross(point2),-19)
        self.assertEqual(point1.cross(point3),-5)
        self.assertNotEqual(point1.cross(point3),0)

    def test_length(self) : 
        point1 = Point(1,0)
        point2 = Point(2,-1)
        point3 = Point(-1,4)

        self.assertEqual(point1.length(),math.sqrt(1))
        self.assertEqual(point3.length(),math.sqrt(17))
        self.assertEqual(point2.length(),math.sqrt(5))
        self.assertNotEqual(point1.length(),0)

if __name__ == '__main__':
    unittest.main()