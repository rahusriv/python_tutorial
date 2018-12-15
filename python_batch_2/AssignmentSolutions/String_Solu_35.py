

while(True):
    try:
        num_string = input("Enter an integer :")
        num_integer = int(num_string)
        print("Its a correct integer")
        print("Success")
        break
    except:
        print("Its NOT an integer. Enter correct integer. Enter again.")
