data = input("Please enter a string :")

reverse1 = data[-1::-1]
reverse2 = data[len(data)-1::-1]

print("Reversed string using method 1 is {}".format(reverse1))
print("Reversed string using method 2 is {}".format(reverse2))

mystring = "abcdefghif"
print(mystring[:2]+mystring[2:])