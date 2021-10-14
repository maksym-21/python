import re

# Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. 
# Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.


def function(str,flag:bool) :
    list = re.findall(r'\S+',str)
    s = ""
    
    for i in list:
         if(flag) : s+= i[0]
         else : s += i[-1]

    return s

print("pls give me input:\n")

line = input()

print("input -> ", line)
print("output#1 -> ", function(line,True))
print("output#2 -> ", function(line,False))
