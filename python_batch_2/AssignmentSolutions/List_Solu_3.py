import sys

mylist = [39, 24, 50 ,200,70 , 1]

#max = -sys.maxsize - 1
#max = -1000000
max = mylist[0]
for item in mylist:
    if item > max:
        max = item

print(max)
