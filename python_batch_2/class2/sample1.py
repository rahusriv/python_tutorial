a = (5== 5)
print(a)
b=3
c=4
d=50
if (c > b):
    print(c)
    print(b)
    if(d>b):
        print(d)
        print("I am in nested ifelse")
    print("I am in if but not in nested if")
else:
    print(a)
    print("I am in else")
    print("I am not in else")