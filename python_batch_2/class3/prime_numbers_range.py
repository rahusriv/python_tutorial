start = int(input("Enter starting number(>5) :"))
end = int(input("Enter ending number(<100000) :"))
count = 0
for i in range(start,end+1):
    prime = 1
    for j in range(2,i-1):
        if(i%j==0):
            prime =0
            break
    if(prime ==1):
        count = count+1
        print("This {} is prime".format(i))
    else:
        pass
