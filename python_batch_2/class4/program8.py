mylist = ["horse","wild boar", "sheep", "tiger"]

ind = mylist.index("tiger")

print(ind)

mylist.remove("sheep")

print(mylist)

ind = mylist.index("tiger")

print(ind)

del mylist[0]

print(mylist)

del mylist

print("#"*50)

list1 = [1,2,3]
list2 = list1
del list1
print(list2[0])