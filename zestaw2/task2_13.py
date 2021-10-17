#Znaleźć łączną długość wyrazów w napisie line.

def function(s) :
    out = [len(j) for j in s.split()]
    return sum(out)

print(function("he\nj a  1\t2"))