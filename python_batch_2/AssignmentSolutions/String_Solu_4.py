para = input("Enetr a paragraph : ")

first = para[0]
result = ""

i =0
for c in para:
    if i ==0:
        result = result + c
    else:
        if c == first:
            result = result + "$"
        else :
            result = result + c

    i = i+1



print(result)

