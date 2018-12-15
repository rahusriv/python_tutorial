num1 = int(input("Please input first number : "))
num2 = int(input("Please input second number : "))

if num1   > num2 :
    print("{} is greater than {}".format(num1,num2))
elif num1 == num2:
    print("{} is equal to {}".format(num2,num1))
else:
    print("{} is greater than {}".format(num2,num1))