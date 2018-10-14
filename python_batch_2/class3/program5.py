n = int(input("Enter n : "))
x = int(input("Enter x : "))

count = 0
for i in range(0,n+1):
    if(i%x ==0):
        count = count +1

print("{} numbers between (0 to {})are divisible by {}".format(count,n,x))