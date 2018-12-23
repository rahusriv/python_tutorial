mylist = [1,1,1,1,1,3,4,4,4,4,3,3,3,5,2,2,2,5,5,1,1,1,2,2,2,3,3,4,4,5,5,2,2]

mydict = {}

for item in mylist:
    mydict[item] = "Random stuff"

res = list(mydict.keys())

print(res)

