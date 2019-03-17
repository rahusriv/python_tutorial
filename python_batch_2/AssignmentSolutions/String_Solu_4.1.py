para = input("Enetr a paragraph : ")

first = para[0]

result = para[0]

for i in range(1,len(para)):
    if first == para[i]:
        result = result + "$"
    else:
        result = result+ para[i]

print(result)