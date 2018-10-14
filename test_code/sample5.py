#Check if a string is a palindrome or not

mystring = input("Please enter a string you want to check :")

rev = mystring[-1::-1]

if(mystring == rev):
    print("Its a palindrome")
else:
    print("Its not a palindrome")

