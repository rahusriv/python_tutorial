a = int(input("Please input first number:"))
b = int(input("Please enter second number"))

c = a%b

print(c)

if c == 0:
    print("{} is divisible by {}".format(a,b))
else:
    print("{} is not divisible by {}".format(a,b))