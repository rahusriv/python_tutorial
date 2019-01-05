def fun1(flag,*args):
    if flag == 0:
        mult = 1
        for item in args:
            mult = mult * item
        return mult
    sum = 0
    for item in args :
        sum = sum + item
    return sum

def fun2(flag,*args, **kwargs):
    print(kwargs)
    print(args)
    if "name" in kwargs:
        print("Your name is : {}".format(kwargs["name"]))
    else:
        print("Name not found")

res = fun2(1,2,3,data="this sentence",name = "Mukund", salary = 1000)