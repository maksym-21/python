def flatten(L:list) :
    output = []
    
    for i in L : 
        if isinstance(i,list) or isinstance(i,tuple) :
            output += flatten(i)
        else : output.append(i)
    
    return output

print(flatten([1,[2,[4]],3]))