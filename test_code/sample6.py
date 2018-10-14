#Finding lenght of a string
mystring = input("Please enter a short string")

lenght = len(mystring)

if(lenght > 20):
    print("String is too long")
else:
    print("String lenght is {} ".format(lenght))