def odwracanie(L, left, right) :
    l = list(L)

    j = int(left)
    k = int(right)

    l[j:k+1] = l[j:k+1][::-1]

    return l

def function(L,left,right) :
    helpful = L[right]
    L[right] = L[left]
    L[left] = helpful
    if left < right and right - left != 1 : return function(L,left+1,right-1)
    else : return L

print(odwracanie([1,2,3,4],1,3))
print(function([1,2,3,4],1,3))

