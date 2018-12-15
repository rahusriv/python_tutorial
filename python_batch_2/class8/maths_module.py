def add(a,b):
    return a+b

def factorial(n):
    if(n>10):
        return 0

    mult = 1
    for i in range(1,n+1):
        mult = mult * i
    return mult


if __name__=="__main__":
    print(factorial(5))