def factorial(n:int) :
    if n < 0 : return -1
    elif n == 0 : return 1
    else :
        output = 1
    
        for i in range(n,1,-1) : output *= i

        return output

print(factorial(5))
