mylist = [0,1,2,3,4,5]

for i in range(0,len(mylist),2):
    mylist[i], mylist[i+1] = mylist[i+1], mylist[i]

print(mylist)
