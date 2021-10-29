import math
import unittest

###
# My own library 
def simple(L) :
    while math.gcd(int(L[0]),int(L[1])) > 1 :
        var = math.gcd(L[0],L[1])
        L[0] /= var
        L[1] /= var
    return [int(L[0]),int(L[1])]

def check_div_by_zero(L,R) :
    if L[1] == 0 or R[1] == 0 : raise Exception("You can not divide by zero")

def LCM(a:int,b:int) : # for least common denominator
    if a > b : higher = a
    else : higher = b

    val = higher

    while True : 
        if higher%a == 0 and higher%b == 0 : return higher
        else : higher = val + higher

####
# Task's library
def add_frac(frac1, frac2) : # frac1 + frac2
    check_div_by_zero(frac1,frac2)
    
    if frac1[1] == frac2[1] :
        return simple([frac1[0] + frac2[0],frac1[1]])
    else :
        res = LCM(frac1[1],frac2[1])

        return simple([frac1[0] * int((res / frac1[1])) + frac2[0] * int((res / frac2[1])),res])

def sub_frac(frac1, frac2) : # frac1 - frac2
    check_div_by_zero(frac1,frac2)
    
    if frac1[1] == frac2[1] :
        return simple([frac1[0] - frac2[0],frac1[1]])
    else :
        res = LCM(frac1[1],frac2[1])
        
        return simple([frac1[0]* int(res / frac1[1])  - frac2[0]* int(res / frac2[1]), res])

def mul_frac(frac1, frac2) : # frac1 * frac2
    check_div_by_zero(frac1,frac2)

    return simple([frac1[0]*frac2[0],frac1[1]*frac2[1]])

def div_frac(frac1, frac2) : # frac1 / frac2
    return simple([frac1[0]*frac2[1],frac1[1]*frac2[0]])

def is_positive(frac) : # bool, czy dodatni
    return True if (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0) else False

def is_zero(frac) :  # bool, typu [0, x]
    return True if frac[0] == 0 else False

def frac2float(frac) : # konwersja do float
    check_div_by_zero(frac,[1,1])

    return float(frac[0] / frac[1])

def cmp_frac(frac1, frac2) : # -1 | 0 | +1
    check_div_by_zero(frac1,frac2)

    if frac1[0] == frac2[0] == 0 : return 0
    
    res = LCM(frac1[1],frac2[1])

    if frac1[1] != res :
        frac1[0] *= (res / frac1[1])
        frac1[1] = res    
    if frac2[1] != res : 
        frac1[0] = res / frac2[1]
        frac2[1] = res

    if frac2[0] == frac1[0] : return 0
    elif frac1[0] > frac2[0] : return 1
    else : return -1



class TestFractions(unittest.TestCase):

    def setUp(self) :
        self.zero = [0, 1]

    def test_add_frac(self) :
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([0, 2], [0, 3]), [0, 1])
        self.assertEqual(add_frac([1, 1], [-3, 2]), [-1, 2])
        # self.assertRaises(Exception,add_frac([1,0],[1,3]))

    def test_sub_frac(self) : 
        self.assertEqual(sub_frac([1,1],[2,2]),[0,1])
        self.assertEqual(sub_frac([5,7],[-5,11]),[90,77])
        # self.assertRaises(Exception,sub_frac([1,0],[1,3]))

    def test_mul_frac(self) : 
        self.assertEqual(mul_frac([4,7],[5,9]),[20,63])
        self.assertEqual(mul_frac([4,9],[0,9]),[0,1])
        self.assertEqual(mul_frac([5,10],[5,20]),[1,8])
        # self.assertRaises(Exception,mul_frac([1,0],[1,3]))

    def test_div_frac(self) :
        self.assertEqual(div_frac([1,3],[2,5]),[5,6])
        self.assertEqual(div_frac([7,8],[1,1]),[7,8])

    def test_is_positive(self) : 
        self.assertFalse(is_positive([0,9]))
        self.assertTrue(is_positive([1,9]))
        self.assertTrue(is_positive([-1,-9]))
        self.assertFalse(is_positive([-1,9]))
        self.assertFalse(is_positive([1,-9]))

    def test_is_zero(self) : 
        self.assertEqual(is_zero([1,1]),False)
        self.assertEqual(is_zero([0,1]),True)

    def test_cmp_frac(self) : 
        self.assertEqual(cmp_frac([0,22],[0,11]),0)
        self.assertEqual(cmp_frac([1,2],[2,4]),0)
        self.assertEqual(cmp_frac([1,2],[1,2]),0)
        
        self.assertEqual(cmp_frac([1,2],[0,2]),1)
        self.assertEqual(cmp_frac([0,2],[7,2]),-1)

    def test_frac2float(self) : 
        self.assertEqual(frac2float([0,2]),float(0))
        self.assertEqual(frac2float([1,2]),float(1/2))
        # self.assertRaises(Exception,frac2float([1,0]))

    def tearDown(self) : pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy