myfile = open("/home/rahul/Desktop/sample.txt","r")
#data = myfile.readlines()

#size = len(data)

#start = size - 10

#for i in range(start,size):
#    print(data[i])

##########################3

size = 0
while(myfile.readline()):
    size = size + 1
print(size)

myfile = open("/home/rahul/Desktop/sample.txt","r")

shift = size - 10

for i in range(0,shift):
    myfile.readline()

line = myfile.readline()
while(line):
    print(line)
    line = myfile.readline()