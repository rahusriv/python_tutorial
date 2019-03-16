n = int(input("Enter a integer limit: "))
num = int(input("By which number you want to divide: "))

i =0
output_string = "Numbers divisible by {} between 0 to {} are :".format(num,n)
while(True):
    if (i>=100 and i<=200):
        i = i+1
        continue
    if(i%num == 0):
        #print(i)
        output_string = output_string + str(i) + ","
        #print(output_string)
        #print(output_string)
    i = i+1
    if i>n:
        break

print(output_string[:-1])