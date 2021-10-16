list =  [[],[4,1],(1,3),[3],(5,6,7,0)]

def function(L:list) :
    output = []        

    for i in L:
        output.append(sum(i))

    return output    


print(function(list))