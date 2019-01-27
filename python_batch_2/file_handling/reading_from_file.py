#Reading from a file

myfile = open("sample.txt","r")

data = myfile.read()

print(data.split("\n"))

myfile.close()

print("*"*100)
myfile = open("sample.txt","r")
data = myfile.readlines()
print(data)

myfile.close()

print("*"*100)
myfile = open("sample.txt","r")

line = myfile.readline()
while(line):
    print(line)
    line = myfile.readline()

myfile.close()
