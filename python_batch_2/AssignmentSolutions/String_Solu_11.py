n = int(input("Enter n : "))
m = int(input("Enter m : "))

result_list = []
tmp = []

for i in range(0,n):
    tmp = []
    for j in range(0,m):
        tmp.append(i*j)
        print(i*j)
    result_list.append(tmp)
    #tmp.clear()

print(result_list)


