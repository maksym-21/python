matrix = { (0, 0) : 0.5 }

def P(i, j) :
    if i < 0 or j < 0 : raise Exception("Arguments must be greater or equal to zero")
    if (i, j) in matrix.keys() : return matrix.get((i, j))

    if i > 0 and j == 0 : return 0.0
    elif i == 0 and j > 0 : return 1.0
    elif i > 0 and j > 0 :
        matrix[(i, j)] = 0.5 * (P(i - 1, j) + P(i, j - 1))

        return matrix.get((i, j))

#
#def P(i:int, j:int) :
#    matrix = [[0 for x in range(10)] for x in range(5)]
#
#    if i == j == 0 : 
#        matrix[i][j] = 0.5
#        return matrix[i][j]
#    elif i > 0 and j == 0 : 
#        matrix[i][j] = 0.0
#        return matrix[i][j]
#    elif j > 0 and i == 0 : 
#        matrix[i][j] = 1.0
#        return matrix[i][j]
#    elif i > 0 and j > 0 : 
#        matrix[i][j] = 0.5 * (P(i-1, j) + P(i, j-1))
#        return matrix[i][j]
#    else : raise ValueError('Something went wrong:(')


print(P(0,0)) # 0.5
print(P(1,0)) # 0.0
print(P(0,1)) # 1.0
print(P(3,1)) # 0.125
