mystring = input("Enter a string :")
#num = int(input("Enter a number"))
num = len(mystring)
#Counting from 0 and incremrenting
i=0
while(i<num):
    print(mystring[i])
    i = i+1
print("*"*50)
#Counting from num and decremenbting
i=num
while(i>0):
    print(mystring[num-i])
    i=i-1