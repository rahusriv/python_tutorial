list_x = []

for i in range(0,3):
    tmp = []
    for j in range(0,4):
        tmp1 = []
        for k in range(0,6):
            tmp1.append("*")
        tmp.append(tmp1)

    list_x.append(tmp)


print(list_x)