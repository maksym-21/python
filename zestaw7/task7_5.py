import unittest
import math as m

from task6_2 import Point

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0 : raise ValueError("Promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self) : # "Circle(x, y, radius)"
        return f'Circle({self.pt.x}, {self.pt.y}, {self.radius})'

    def __eq__(self, other) :
        return self.pt==other.pt and self.radius == other.radius

    def __ne__(self, other) :
        return not self == other

    def area(self) : # pole powierzchni
        return m.pi * self.radius**2

    def move(self, x, y) : # przesuniecie o (x, y)
        if x !=None and y!=None : 
            self.pt = Point(self.pt.x + x,self.pt.y + y)

    def cover(self, other) : # najmniejszy okrąg pokrywający oba
        coords_of_new_rad = self.pt if self.area() > other.area() else other.pt

        rad = self.radius if self.area() > other.area() else other.radius

        whole_dist_b_2r = m.sqrt((self.pt.x - other.pt.x)**2 + (self.pt.y - other.pt.y)**2)

        if rad != self.radius : smallest_d = self.radius 
        else : smallest_d = other.radius

        return Circle(coords_of_new_rad.x, coords_of_new_rad.y, whole_dist_b_2r + smallest_d)


class TestCircle(unittest.TestCase): 
    def test_repr(self) :
        c1 = Circle(0,0,2)

        self.assertEqual(c1.__repr__(),'Circle(0, 0, 2)')

        c1 = Circle(1,-1,3)

        self.assertEqual(c1.__repr__(),'Circle(1, -1, 3)')

    def test_eq(self) :
        c1 = Circle(0,0,2)
        c2 = Circle(1,1,2)
        c3 = Circle(1,1,2)
        c4 = Circle(1,1,3)

        self.assertFalse(c1.__eq__(c2))
        self.assertTrue(c2.__eq__(c3))    
        self.assertFalse(c3.__eq__(c4)) 

    def test_ne(self) :
        c1 = Circle(0,0,2)
        c2 = Circle(0,0,2)

        self.assertFalse(c2.__ne__(c2))
        self.assertFalse(c2.__ne__(c1)) 

    def test_area(self) : 
        c1 = Circle(0,0,2)
        c2 = Circle(0,0,1)

        self.assertNotEqual(c1.area(),0)
        self.assertEqual(c1.area(),m.pi*4)
        self.assertEqual(c2.area(),m.pi)

    def test_move(self) :
        c1 = Circle(1,1,3)

        c1.move(-1,-1)
        self.assertEqual(c1.pt, Point(0,0) )

        c1.move(2,2)
        self.assertNotEqual(c1.pt, Point(0,0) )
        self.assertEqual(c1.pt, Point(2,2))

    def test_cover(self) :
        c1 = Circle(-2, 2, 1)
        c2 = Circle(2, 0, 2)
        c3 = Circle(-2, 0, 2)

        self.assertEqual(c1.cover(c2), Circle(2, 0, 1 + m.sqrt(20) ))
        self.assertEqual(c2.cover(c3), Circle(-2, 0, 6))

if __name__ == '__main__':
    unittest.main()           