def modifyInt(a):
    #print(a)
    a = 55
    #print(a)

def modifyFloat(b):
    b = 9.9

def modifyString(c):
    c = "Modified"

def modifyList(l):
    l.clear()
    l.append("Changed")
    l.append("000")
    l.append(100)

def modifyDict(d):
    d[3] = "three"

num1 = 100
print("Before modification {}".format(num1))
modifyInt(num1)
print("After modification {}".format(num1))


num2 = 100.55
print("Before modification {}".format(num2))
modifyFloat(num2)
print("After modification {}".format(num2))

var3 = "Original"
print("Before modification {}".format(var3))
modifyString(var3)
print("After modification {}".format(var3))

var4 = [1,2,3,4,5]
print("Before modification {}".format(var4))
modifyList(var4)
print("After modification {}".format(var4))

var5 = {1:"one", 2: "two"}
print("Before modification {}".format(var5))
modifyDict(var5)
print("After modification {}".format(var5))



