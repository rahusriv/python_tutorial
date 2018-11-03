
def modifyInteger(a):
    #print(a)
    a = 100
    #print(a)

def modifyFloat(b):
    b=2.5

def modifyString(s):
    s = "Modified this"

def modifyList(l):
    l.append("Addeed new value")

def modifyDictionary(d):
    d[10]="Ten"

a = 10
print("Before function call : a = {}".format(a))
modifyInteger(a)
print("After function call : a = {}".format(a))

print("*"*50)

b = 10.5
print("Before function call : b = {}".format(b))
modifyFloat(b)
print("After function call : b = {}".format(b))

print("*"*50)
s = "Original"
print("Before function call : s = {}".format(s))
modifyString(s)
print("After function call : s = {}".format(s))

print("*"*50)
l = ["First", "Second"]
print("Before function call : l = {}".format(l))
modifyList(l)
print("After function call : l = {}".format(l))

print("*"*50)
d = {1:"One",2:"Two"}
print("Before function call : d = {}".format(d))
modifyDictionary(d)
print("After function call : d = {}".format(d))


