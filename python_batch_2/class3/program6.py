
n = int(input("Please enter a number :"))

prime = 1

#for i in range(2,n):
#    if(n%i ==0):
#        prime = 0
#        break

i = 2
while(True):
    if(n%i==0):
        prime=0
        break

    if(i==n-1):
        break
    i = i+1






if(prime ==1):
    print("{} is a prime number. ".format(n))
else:
    print("{} is NOT a prime number".format(n))

