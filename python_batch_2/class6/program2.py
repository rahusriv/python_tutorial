
def multiplyTwoNumbers(a,b):
    res = a*b
    #print(res)
    return res

def factorial(n):
    res =1
    for i in range(2,n+1):
        res = res *i
    return res

a=10
b=20
res = multiplyTwoNumbers(a,b)

print(res)

n=5
res = factorial(n)
print(res)