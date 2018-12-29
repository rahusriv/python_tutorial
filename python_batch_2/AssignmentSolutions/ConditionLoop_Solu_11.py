m = int(input("Enter rows :"))
n = int(input("Ebter columns: "))

twodlist = []

for i in range(0,m):
    tmp = []
    for j in range(0,n):
        tmp.append(i*j)
    twodlist.append(tmp)

print(twodlist)