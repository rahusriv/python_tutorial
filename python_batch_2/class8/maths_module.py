def add(a,b):
    return a+b

def factorial(n):
    if(n>10):
        return 0

    mult = 1
    for i in range(1,n+1):
        mult = mult * i
    return mult

def driverFunction():
    num1 = int(input("Num 1: "))
    num2 = int(input("Num 2: "))
    print("Sum = {}".format(add(num1,num2)))
    print("Factorial of sum = {}".format(factorial(add(num1, num2))))
#driverFunction()
if __name__=="__main__":
    driverFunction()