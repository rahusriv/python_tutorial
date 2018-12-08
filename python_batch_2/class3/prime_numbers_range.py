

start = int(input("Enter starting number(>5) :"))
end = int(input("Enter ending number(<100000) :"))
count = 0
output_string = ""
for i in range(start,end+1):
    prime = 1
    for j in range(2,i-1):
        if(i%j==0):
            prime =0
            break
    if(prime ==1):
        count = count+1
        if(count%10 ==0):
            output_string = output_string + "\n"
        output_string = output_string + "  "+str(i)
        #print("This {} is prime".format(i))
    else:
        pass

print(" Total {} prime numbers found. They are given below: ".format(count))
print(output_string)
file = open("prime_numbers_{}_{}.txt".format(start,end),"w")
file.write(output_string)