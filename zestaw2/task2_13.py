#Znaleźć łączną długość wyrazów w napisie line.

def function(str) :
    return len(str) - str.count(" ")

print("pls give me input:\n")

line = input()

print("input -> ", line)
print("output -> ", function(line))