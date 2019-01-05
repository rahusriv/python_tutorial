mydict = {5443:"Rahu", 7786: "Jimmy", 8762:"Manasha",6675:"Mukund", 9876:"Sheshadri"}

mylist = []
mylist = list(mydict.values())

mylist.sort()

print(mylist)

reversedict = {}

for key in mydict:
    val = mydict[key]
    reversedict[val] = key

result = []
for item in mylist:
    tmp = []
    tmp.append(item)
    tmp.append(reversedict[item])
    result.append(tmp)

print(result)

