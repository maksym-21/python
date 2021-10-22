# def sum_seq(l:list) 
def sum_seq(L:list) :
    output = 0
    
    for i in L : 
        if isinstance(i,list) or isinstance(i,tuple) :
            output += sum_seq(i)
        else : output += i    
    
    return output    

print(sum_seq([1,[2,[4]],3]))