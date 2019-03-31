def factorial(n):
    if type(n).__name__ != "int":
        return -1

    product = 1
    for i in range(1,n+1):
        product = product * i
    return product

def max(a,b):
    if a> b:
        return a
    else:
        return b

def average(list_numbers):
    sum = 0
    for num in list_numbers:
        sum = sum + num
    return sum/len(list_numbers)

def testFactorial():
    n = int(input("Enter a number : "))
    res = factorial(str(n))
    print(res)

#testFactorial()
if __name__ == '__main__':
    print(__name__)
    testFactorial()
    sum = 5