#Take inpur form user name and addree
#and print "Hello , <user name>, your address is <address>"
#.format() of string to acheive this task

name = input("Please enter your name:")
add = input("Please input your address: ")

myoutput = "Hello, your name is {0}, and your address is {1}, {2}, agin my address is {1} and my name is {0}"#.format(name,add)
myoutput_new = myoutput.format(name,add,"  some random stuff ")

print(myoutput)
print(myoutput_new)

print("Value od pi: {0:0.5}".format(2200/7))