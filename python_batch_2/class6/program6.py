# 0, 1, 1, 2, 3, 5, 8, 13 ...


def fib(n):
    if n ==0:
        return 0

    if n==1:
        return 1

    return fib(n-1)+fib(n-2)


num = int(input("Enter a number : "))

res = fib(num)

print(res)