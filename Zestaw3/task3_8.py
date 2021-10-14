list1 = ["kk","kkk","kk",1,2,3,"hej","kk"]
list2 = ["k","kk","asdf",5,6,1,"hejka","kk"]

set1 = set(list1)
set2 = set(list2)

inter = set1.intersection(set2)

sum = set1 | set2

print(inter)
print(sum)