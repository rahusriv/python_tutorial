mydict = {5443:"Rahu", 7786: "Jimmy", 8762:"Manasha",6675:"Mukund", 9876:"Sheshadri"}
print(mydict)
mylist = []
mylist = list(mydict.values())

mylist.sort()

print(mylist)

reversedict = {}

for key in mydict:
    val = mydict[key]
    reversedict[val] = key

print(reversedict)

result = []
for item in mylist:
    tmp = {}
    tmp[reversedict[item]] = item
    #tmp.append(reversedict[item])
    result.append(tmp)

print(result)

