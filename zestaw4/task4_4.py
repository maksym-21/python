def fibonacci(n:int) :
    if n <= 0 :
        print("pls try with a positive number")
        return -1
    elif n == 1 :
        return 1
    else :
        output, count = 0, 0
        # let f(0) = n0 = 0 and f(1) = n1 = 1
        n0, n1 = 0, 1
        
        while count < n :
            output = n0 + n1

            n0 = n1
            n1 = output

            count += 1

        return output - 1

print(fibonacci(6))
print(fibonacci(7))
