#Looping in a list

mylist = [4,7,10,245,79,100]

#Find the number divisible by 10

for i in range(0,len(mylist)):
    if mylist[i]%10 == 0:
        print(mylist[i])

print("*"*50)

#print all elements of the list
for i in range(0,len(mylist)):
    print(mylist[i])

print("*"*50)

for item in mylist:
    if item%10==0:
        print(item)