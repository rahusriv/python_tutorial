while(True):
    try:
        num = int(input("Please enter a number b/w 1 to 10"))
        if num >= 1 and num <=10:
            print("Correct input")
            break
        else:
            continue
    except:
        continue
    #list1 = [1,2,3,4,5,6,7,8,9,10]