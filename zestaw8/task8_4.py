import math as m

def heron(a, b, c):
    if a < b+c and b < a+c and c < a+b : 
        p = (a + b + c) /2

        return m.sqrt(p * (p-a) * (p-b) * (p-c))
    else : return ValueError("It's not a triangle")

print(heron(5,4,3))  