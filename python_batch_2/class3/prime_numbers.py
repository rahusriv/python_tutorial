num = int(input("Type a number >5:"))
prime =1
for i in range(2,num-1):
    if(num%i == 0):
        #print("Number is not prime")
        prime = 0
        break

if prime ==1 :
    print("Its a prime number")
else :
    print("Its NOT a prime number")