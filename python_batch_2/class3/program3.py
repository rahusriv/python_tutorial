
data = input("Enter a string , I will extract all numbers from it !   ")

res = ""

for c in data:
    if(c in "0123456789"):
        res = res + c

print(res)