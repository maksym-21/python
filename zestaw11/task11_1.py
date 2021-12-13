import random as r

# różne liczby int od 0 do N-1 w kolejności losowej
def rand_array_not_sort(n:int) :
    return [r.randint(0,n-1) for j in range(n)]

# różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji)
def rand_array_rand_sort(n:int, randRange:int) :
    return [r.randint(j-randRange, j+randRange) for j in range(n)]

# różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności
def rand_array_rand_sort_reversed(n:int, randRange:int) :
    return [r.randint(j-randRange, j+randRange) for j in reversed(range(n))]

# N liczb float w kolejności losowej o rozkładzie gaussowskim
def rand_float_gauss(n:int) :
    return [r.gauss(0,1) for j in range(n)]

# N liczb int w kolejności losowej, o wartościach powtarzających się, 
# należących do zbioru k elementowego (k < N, np. k*k = N)
def rand_int_array(n:int) :
    array = []
    my_set = rand_array_not_sort(r.randint(1, n - 1))
    
    for j in range(n) : 
        array.append(my_set[r.randint(0,len(my_set) - 1)])

    return array    
