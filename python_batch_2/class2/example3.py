raining = int(input("Is it raining ? (0: not raining , 1: raining)"))
holiday = int(input("Do you have a holiday ? (0: no holiday, 1: holiday)"))
'''
if raining ==0:
    if holiday ==1:
        print("You can jog")
    else:
        print("You cant jog")
else:
    print("You can not jog")

'''
if raining == 0 and holiday ==1:
    print("You can jog")
else:
    print("You cnanot jog")