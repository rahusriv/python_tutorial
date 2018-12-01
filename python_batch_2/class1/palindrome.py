original_string = input("Please input a string ? ")

reverse = original_string[-1::-1]

if reverse == original_string:
    print("Its a palindrome .")
else:
    print("Its not a palindrome")