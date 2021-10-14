# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej.

var = 123040540560
counter = 0
for i in map(int,str(var)) : 
    if i==0 : counter+=1

print(counter)

