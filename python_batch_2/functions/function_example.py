def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res * i

    return res

num = int(input("Enter a number : "))
res1 = factorial(num)
print("Factorial of {} is {} :".format(num,res1))
