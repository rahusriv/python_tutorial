dict1= {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60,7:70,8:80}

mylist = []
mylist.append(dict1)
mylist.append(dict2)
mylist.append(dict3)

result = {}

for mydict in mylist:
    for key in mydict:
        result[key] = mydict[key]


print(mylist)
print(result)