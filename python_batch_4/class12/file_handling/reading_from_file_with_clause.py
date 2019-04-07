#Reading from a file

with open("sample.txt","r") as myfile:
    data = myfile.read()
    print(data.split("\n"))

print("*"*100)

with open("sample.txt","r") as myfile:
    data = myfile.readlines()
    print(data)

print("*"*100)

with open("sample.txt","r") as myfile:
    line = myfile.readline()
    while(line):
        print(line)
        line = myfile.readline()
