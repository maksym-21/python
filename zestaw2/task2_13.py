#Znaleźć łączną długość wyrazów w napisie line.

def function(s) :
    return len(s) - s.count("\s")

print("pls give me input:\n")

line = input()

print("input -> ", line)
print("output -> ", function(line))