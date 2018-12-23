mylist = [0,0,1,1,1,1,1,2,2,2,2,3,3,3,1,1,1,4,4,4,5,5,5,5,2,3,4,5,6,6,7,7,8,8,9,9,10,10,1,2,3,4,5,6,6,7,10,10,9,8,4,5]

#outputstring = "Tell me a number :"

#num = int(input(outputstring))
frequency = {}      #{1:21,2:15,3:11}

for num in mylist:
    if num in frequency:
        val = frequency[num]
        val = val+1
        frequency[num] = val
    else:
        frequency[num] = 1

print(frequency)


outputstring = "Tell me a number :"

num = int(input(outputstring))

if num in frequency:
    print("Frequency of {} is {} ".format(num,frequency[num]))
else:
    print("Sorry {} dosent exist".format(num))


