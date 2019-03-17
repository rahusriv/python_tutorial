line = input("Enetr a string : ")

index_comma = 0 #line.index(",")
index_dot = 0 #line.index(".")

i = 0
for c in line:
    if(c == ","):
        index_comma = i
        break
    i = i+1

i = 0
for c in line:
    if(c == "."):
        index_dot = i
        break
    i = i+1
res = ""
if(index_comma < index_dot):
    res = line[0:index_comma] + "."+line[index_comma+1:index_dot] + ","+line[index_dot+1:]
else:
    res = line[0:index_dot] + ","+line[index_dot+1:index_comma] + "."+line[index_comma+1:]

print(res)