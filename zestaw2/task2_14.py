import re

# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.

def most_len(str):
    return max(re.findall(r'\S+',str),key=len)

def most_int(str):
    return len(most_len(str))

print("pls give me input:\n")

var = input()

print("input -> ", var)
print("a -> ", most_len(var))
print("b -> ", most_int(var))

