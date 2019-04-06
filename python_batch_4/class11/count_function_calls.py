count = 0
count1 = 0
count2 = 0
count3 = 0

def fun1():
    global count1
    count1 = count1 +1
    print("fun1 called")

def fun2():
    global count2
    count2 = count2 +1
    print("fun2 called")

def fun3():
    global count3
    count3 = count3 +1
    print("fun3 called")


fun1()
fun2()
fun3()
fun1()
fun1()
fun1()
fun3()
fun3()
fun2()
fun2()

print("Total calls = {}".format(count))
print("Total calls = {}".format(count1))
print("Total calls = {}".format(count2))
print("Total calls = {}".format(count3))