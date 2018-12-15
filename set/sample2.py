set1 = {2,2,4,6,8,10,12,14,16,18,20}
set2 = {5,10,15,20}

#set1 = set(list1)
#set2 = set(list2)
#print(set1)
set3 = set1.intersection(set2)
set4 = set1.union(set2)

set1.difference(set2)
print(set1)
set1.difference_update(set2)
print(set1)
#print(set3)
#print(set4)
#print(set5)