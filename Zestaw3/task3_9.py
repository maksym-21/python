list =  [[],[4,1],(1,3),[3],(5,6,7,0)]

def function(l:list):
    output = []        

    for i in range(len(l)):
        output.append(sum(l[i]))

    return output    


print(function(list))