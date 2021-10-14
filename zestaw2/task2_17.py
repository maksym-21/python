import re

# Posortować wyrazy z napisu line raz alfabetycznie, 
# a raz pod względem długości.

line = input()

list = re.findall(r'\S+',line)

print("output#1 -> ",sorted(list,key=str.lower))
print("output#2 -> ",sorted(list,key=len))


