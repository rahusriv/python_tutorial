
count = 0

def counter1(b):
    global count
    print("Count 1 called")
    count = count +1

def counter2(c):
    global count
    print("Count 2 Function called ")
    count = count +1

def printTotalCalls():
    print("Total calls made = {}".format(count))

#print(a)
counter1(20)
counter1(20)
counter1(20)
counter1(20)
counter1(20)

counter2(20)
counter2(20)
counter2(20)

printTotalCalls()

