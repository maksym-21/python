from task6_2 import Point
import math
import unittest

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self) : # "[(x1, y1), (x2, y2)]"
        return f'[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]'

    def __repr__(self) : # "Rectangle(x1, y1, x2, y2)"
        return f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

    def __eq__(self, other) : # obsługa rect1 == rect2
        len1 = math.fabs(self.pt2.x - self.pt1.x)
        high1 = math.fabs(self.pt2.y - self.pt1.y)

        len2 = math.fabs(other.pt2.x - other.pt1.x)
        high2 = math.fabs(other.pt2.y - other.pt1.y)

        return True if ((len1 == len2 and high1 == high2) or (len1 == high2 and high1 == len2)) else False

    def __ne__(self, other) : # obsługa rect1 != rect2
        return not self == other

    def center(self) : # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2,(self.pt1.y + self.pt2.y) / 2)

    def area(self) : # pole powierzchni
        return math.fabs(self.pt2.x - self.pt1.x) * math.fabs(self.pt2.y - self.pt1.y)

    def move(self, x, y) : # przesunięcie o (x, y)
        self.pt2 = Point(self.pt2.x + x,self.pt2.y + y)
        self.pt1 = Point(self.pt1.x + x,self.pt1.y + y)


class TestRectangle(unittest.TestCase) : 
    def test_str(self) :
        r1 = Rectangle(-2,-4,2,-2)

        self.assertEqual(r1.__str__(),"[(-2, -4), (2, -2)]")

        r2 = Rectangle(0,0,2,2)

        self.assertEqual(r2.__str__(),"[(0, 0), (2, 2)]")

    def test_repr(self) : 
        r1 = Rectangle(-1,0,2,-1)

        self.assertEqual(r1.__repr__(),"Rectangle(-1, 0, 2, -1)")

        r2 = Rectangle(1,0,2,2)
        # Rectangle(
        self.assertEqual(r2.__repr__(),"Rectangle(1, 0, 2, 2)")

    def test_eq(self) :
        r1 = Rectangle(0,0,2,2)
        r2 = Rectangle(-2,-2,0,0)

        self.assertTrue(r1.__eq__(r2))
        self.assertTrue(r2.__eq__(r1))

        r3 = Rectangle(-2,-2,2,2)

        self.assertFalse(r1.__eq__(r3))
        self.assertFalse(r2.__eq__(r3))
        self.assertFalse(r3.__eq__(r2))

    def test_ne(self) : 
        #fgnfnkll;l;
        r1 = Rectangle(0,0,2,2)
        r2 = Rectangle(-2,-2,0,0)

        self.assertTrue(r1.__eq__(r2))
        self.assertTrue(r2.__eq__(r1))

        r3 = Rectangle(-2,-2,2,2)

        self.assertFalse(r1.__eq__(r3))
        self.assertFalse(r2.__eq__(r3))
        self.assertFalse(r3.__eq__(r2))

    def test_center(self) :
        r1 = Rectangle(0,0,2,2)
        r2 = Rectangle(-2,-2,0,0)

        self.assertNotEqual(r1.center(),Point(0,0))
        self.assertNotEqual(r2.center(),Point(0,0))
        
        self.assertEqual(r1.center(),Point(1,1))
        self.assertEqual(r2.center(),Point(-1,-1))

    def test_area(self) :
        r1 = Rectangle(1,1,2,2)
        r2 = Rectangle(-2,-2,1,1)

        self.assertNotEqual(r1.area(),0)
        self.assertNotEqual(r1.area(),2)

        self.assertEqual(r1.area(),1)
        self.assertEqual(r2.area(),9)
        
    def test_move(self) :
        r1 = Rectangle(0,0,2,2)

        r1.move(1,1)
        self.assertEqual(r1.pt1.x,1)
        self.assertEqual(r1.pt1.y,1)
        self.assertEqual(r1.pt2.y,3)
        self.assertEqual(r1.pt2.x,3)

        r2 = Rectangle(-1,-1,2,2)

        r2.move(1,1)
        self.assertNotEqual(r2.pt1.x,-1)
        self.assertNotEqual(r2.pt1.y,-1)
        self.assertNotEqual(r2.pt2.y,2)
        self.assertNotEqual(r2.pt2.x,2)


if __name__ == "__main__" :
    unittest.main()


