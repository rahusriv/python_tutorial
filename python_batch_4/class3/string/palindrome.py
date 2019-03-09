mystring = input("Please enter a string : ")

trimmed_string = mystring.strip()

print(trimmed_string)
#print(trimmed_string)
#print(len(trimmed_string))
#print(len(mystring))
revrese = trimmed_string[len(trimmed_string)-1 ::-1]

print("Original string is {} , and reversed string is {}".format(trimmed_string,revrese))

if trimmed_string == revrese:
    print("Its a palindrome !")
else:
    print("Sorry its NOT a palindrome!")

