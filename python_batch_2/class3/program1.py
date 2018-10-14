#Method 1
#x = int(input("Please enter a number :"))

#n = int(input("Enter any random number :"))

#while(n%x!=0):
#    n = int(input("Enter any random number :"))

#Method 2

x = int(input("Please enter a number :"))

while(True):
    n = int(input("Enter any random number :"))
    if(n%x == 0):
        print("Number {} is divisibleby {}".format(n,x))
        break;
