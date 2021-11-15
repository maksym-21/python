import unittest
import math as m

class Frac:
    """Klasa reprezentująca ułamki."""

    @staticmethod
    def __LCM(a:int,b:int) : # for least common denominator
        if a > b : higher = a
        else : higher = b

        val = higher

        while True : 
            if higher%a == 0 and higher%b == 0 : return higher
            else : higher = val + higher

    @staticmethod
    def __simple(L) :
        while m.gcd(int(L[0]),int(L[1])) > 1 :
            var = m.gcd(L[0],L[1])
            L[0] /= var
            L[1] /= var
        return Frac(int(L[0]),int(L[1]))


    def __init__(self, x=0, y=1) :
        # Sprawdzamy, czy y=0.
        self.x = x
        if y!=0 : self.y = y
        else : raise ValueError("You can not divide by zero")

    def __str__(self) : # zwraca "x/y" lub "x" dla y=1
        if self.y == 1 : return f'{self.x}'
        else : return f'{self.x}/{self.y}'

    def __repr__(self) : # zwraca "Frac(x, y)"
        return f'Frac({self.x}, {self.y})'

    def __cmp__(self, other) : # cmp(frac1, frac2)
        if self.x == other.x == 0 : return 0
    
        res = Frac.__LCM(self.y,other.y)

        if other.y != res :
            other.x *= res / other.y
            other.y = res 
        if self.y != res : 
            self.x *= res / self.y
            self.y = res

        if self.x == other.x : return 0
        elif self.x > other.x : return 1
        else : return -1

    def __eq__(self, other) : 
        fr1 = Frac.__simple([self.x,self.y])
        fr2 = Frac.__simple([other.x,other.y])

        if fr1.y != fr2.y : 
            t = Frac.__LCM(fr1.y,fr2.y)
            return True if fr1.x * (t / fr1.y) == fr2.x * (t / fr2.y) else False
        else : return True if fr1.x == fr2.x else False

    def __ne__(self, other) : 
        fr1 = Frac.__simple([self.x,self.y])
        fr2 = Frac.__simple([other.x,other.y])

        if self.x == other.x == 0 : return False

        if fr1.y != fr2.y : 
            t = Frac.__LCM(fr1.y,fr2.y)
            return False if fr1.x * (t / fr1.y) == fr2.x * (t / fr2.y) else True
        else : return False if fr1.x == fr2.x else True

    def __lt__(self, other) : 
        return True if(self.x/self.y < other.x / other.y) else False

    def __le__(self, other) : 
        return True if(self.x/self.y <= other.x / other.y) else False

    def __gt__(self, other) : 
        return True if(self.x/self.y > other.x / other.y) else False

    def __ge__(self, other) : 
        return True if(self.x/self.y >= other.x / other.y) else False

    def __add__(self, other) : # frac1+frac2, frac+int
        flag = False

        if isinstance(other,int) : flag = True

        if flag :
            return Frac.__simple([self.x + other*self.y,self.y])
        else :
            res = Frac.__LCM(self.y,other.y)

            return  Frac.__simple([self.x * int((res / self.y)) + other.x * int((res / other.y)),res])

    __radd__ = __add__

    def __sub__(self, other) : # frac1-frac2, frac-int
        flag = False

        if isinstance(other,int) : flag = True

        if flag :
            return Frac.__simple([self.x - (other*self.y) ,self.y])
        else : 
            res = Frac.__LCM(self.y,other.y)

            return Frac.__simple([self.x*(res/self.y) - other.x*(res/other.y) ,res])

    def __rsub__(self, other) : # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other) : # frac1*frac2, frac*int
        flag = False

        if isinstance(other,int) : flag = True

        if flag : 
            return Frac.__simple([self.x * other,self.y])
        else : 
            if(self.y * other.y!=0) : return Frac.__simple([self.x * other.x,self.y * other.y]) 
            else : raise ValueError("You can not divide by zero")

    __rmul__ = __mul__

    def __div__(self, other) : # frac1/frac2, frac/int, Python 2
        flag = False

        if isinstance(other,int) : flag = True

        if flag : 
            if other!=0 : return Frac.__simple([self.x,self.y * other])
            else : raise ValueError("You can not divide by zero")
        else : 
            if other.x == 0 or other.y == 0 : raise ValueError("You can not divide by zero")

            return Frac.__simple([self.x*other.y,self.y * other.x])

    def __rdiv__(self, other) :  # int/frac, Python 2
        if other == 0 : return Frac(0,1) # let 0 means 0/1
        return Frac.__simple([other*self.y,self.x])

    def __truediv__(self, other) : # frac1/frac2, frac/int, Python 3
        pass

    def __rtruediv__(self, other) : 
        pass  # int/frac, Python 3

    # operatory jednoargumentowe
    def __pos__(self) : # +frac = (+1)*frac
        return self

    def __neg__(self) : # -frac = (-1)*frac
        return Frac(-self.x,self.y)

    def __invert__(self) : # odwrotnosc: ~frac
        return Frac(self.y,self.x)

    def __float__(self) : # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self)) # immutable fracs

# Kod testujący moduł.

class TestFract(unittest.TestCase) : 
    
    def test_str(self) :
        f1 = Frac(2,1.0)

        self.assertEqual(f1.__str__(),'2')

        f2 = Frac(2,3)

        self.assertEqual(f2.__str__(),'2/3')

    def test_repr(self) :
        f1 = Frac(-2,1)

        self.assertEqual(f1.__repr__(),'Frac(-2, 1)')

        f2 = Frac(3,-4)

        self.assertNotEqual(f1.__repr__(),'Frac(-3, 4)')

    def test_cmp(self) :
        f1 = Frac(0,1)
        f2 = Frac(0,-4)

        self.assertEqual(f1.__cmp__(f2),0)

        f3 = Frac(2,5)

        self.assertEqual(f1.__cmp__(f3),-1)

        f3 = Frac(-1,2)

        self.assertEqual(f2.__cmp__(f3),1)

    def test_eq(self) :
        f1 = Frac(0,1)
        f2 = Frac(0,-4)

        self.assertTrue(f1.__eq__(f2))

        f3 = Frac(2,5)
        f5 = Frac(2,5)

        self.assertTrue(f3,f5)
        self.assertFalse(f1.__eq__(f3))

        f3 = Frac(1,2)
        f4 = Frac(1,-2)

        self.assertFalse(f3.__eq__(f4))

    def test_ne(self) :
        f1 = Frac(0,1)
        f2 = Frac(0,-4)

        self.assertFalse(f1.__ne__(f2))

        f3 = Frac(3,5)

        self.assertTrue(f1.__ne__(f3))

        f3 = Frac(-1,2)
        f4 = Frac(1,-2)

        self.assertFalse(f3.__ne__(f4))

    def test_lt(self) :
        f1 = Frac(0,2)
        f2 = Frac(0,-3)

        self.assertFalse(f1.__lt__(f2))

        f3 = Frac(3,5)

        self.assertTrue(f1.__lt__(f3))

        f3 = Frac(-3,2)
        f4 = Frac(3,-2)

        self.assertFalse(f3.__lt__(f4))

    def test_le(self) :
        f1 = Frac(0,1)
        f2 = Frac(0,3)

        self.assertTrue(f1.__le__(f2))

        f3 = Frac(3,5)

        self.assertTrue(f1.__le__(f3))

        f3 = Frac(-1,2)
        f4 = Frac(1,-2)

        self.assertTrue(f3.__le__(f4))

    def test_gt(self) :
        f1 = Frac(0,1)
        f2 = Frac(0,3)

        self.assertFalse(f1.__gt__(f2))

        f3 = Frac(3,-5)

        self.assertTrue(f1.__gt__(f3))

        f3 = Frac(-1,2)
        f4 = Frac(1,2)

        self.assertFalse(f3.__gt__(f4))

    def test_ge(self) :
        f1 = Frac(0,2)
        f2 = Frac(0,4)

        self.assertTrue(f1.__ge__(f2))

        f3 = Frac(1,-5)

        self.assertTrue(f1.__ge__(f3))

        f3 = Frac(-1,2)
        f4 = Frac(1,3)

        self.assertFalse(f3.__ge__(f4))

    def test_add(self) :
        f1 = Frac(0,3)
        f2 = Frac(1,-5)
        f3 = Frac(-1,2)
        f4 = Frac(2,3)

        w1 = f1.__add__(f2)
        self.assertEqual(w1,Frac(1,-5))
        w2 = f2.__add__(f3)
        self.assertEqual(w2,Frac(7,-10))
        self.assertEqual(f2.__add__(f4),Frac(-7,-15))

    def test_sub(self) :
        f2 = Frac(1,-5)
        f3 = Frac(-1,2)
        f4 = Frac(2,3)

        w1 = f2.__sub__(f3)
        self.assertEqual(w1,Frac(-3,-10))
        self.assertEqual(f3.__sub__(f4),Frac(-7,6))

    def test_rsub(self) :
        f1 = Frac(1,5)
        f2 = Frac(-1,2)

        self.assertEqual(f2.__rsub__(1),Frac(3,2))
        self.assertEqual(f1.__rsub__(2),Frac(9,5))

    def test_mul(self) :
        f1 = Frac(1,5)
        f2 = Frac(-1,2)

        self.assertEqual( f1.__mul__(2) , Frac(2,5) )
        self.assertEqual( f2.__mul__(Frac(2,3)) , Frac(-1,3) )

    def test_div(self) :
        f1 = Frac(1,3)
        f2 = Frac(-2,5)

        self.assertEqual( f1.__div__(2) , Frac(1,6) )
        self.assertEqual( f1.__div__(f2) , Frac(5,-6) )

    def test_rdiv(self) :
        f1 = Frac(1,3)

        self.assertEqual( f1.__rdiv__(2) , Frac(6,1) )
        self.assertEqual( f1.__rdiv__(0) , Frac(0,1) )

    def test_pos(self) :
        f1 = Frac(1,3)

        self.assertEqual( f1.__pos__() , Frac(1,3) )

    def test_neg(self) :
        f1 = Frac(1,3)

        self.assertEqual( f1.__neg__() , Frac(-1,3) )

    def test_invert(self) :
        f1 = Frac(1,2)

        self.assertEqual( f1.__invert__() , Frac(2,1) )

    def test_float(self) :
        f1 = Frac(1,4)
        f2 = Frac(0,4)

        self.assertEqual( f1.__float__() , 1/4)
        self.assertEqual( f2.__float__() , 0)

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

