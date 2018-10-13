a = int(input("First no ? "))
b = int(input("Second no ? "))
c = int(input("Third no ? "))

if(a>b):
    if(c>a):
        print(c)
    else:
        print(a)
else:
    if(c>b):
        print(c)
    else:
        print(b)

