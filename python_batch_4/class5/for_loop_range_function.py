limit = int(input("Enter a integer limit: "))
num = int(input("By which number you want to divide: "))
output_string = "Numbers divisible by {} between 0 to {} are :".format(num,limit)

for i in range(0,limit+1,num):
    if (i>=100 and i<=200):
        continue
    output_string = output_string + str(i) + ","

print(output_string[:-1])
