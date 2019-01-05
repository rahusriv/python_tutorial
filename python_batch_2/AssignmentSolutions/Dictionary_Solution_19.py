d1 = {"a": 100, "b":200, "c":300, "z":500}
d2 = {"a": 300, "b": 200, "c": 400,"d":900}

mylist = []
mylist.append(d1)
mylist.append(d2)

result = {}

for mydict in mylist:
    for key in mydict:
        if key in result:
            val1 = result[key]
            val2 = mydict[key]
            result[key] = val1+val2
        else:
            result[key] = mydict[key]

print(result)