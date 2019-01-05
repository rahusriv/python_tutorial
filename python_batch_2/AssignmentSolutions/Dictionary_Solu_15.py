mydict = {1:10,2:20,3:5,4:11,5:78,6:100,7:3,8:5,9:10,10:25}

min = 1000000
max = -1000000

for key in mydict:
    val = mydict[key]
    #max
    if val > max :
        max = val
    #min
    if val < min :
        min = val

print(max)
print(min)