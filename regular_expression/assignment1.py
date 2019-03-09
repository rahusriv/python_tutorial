import re

def checkFileType(line):
    line = line.strip()
    p = re.compile(r"(\.)([t])([x])([t])",re.IGNORECASE)
    m = p.search(line)
    if m is None:
        print("File {} did not match ".format(line))
        return 0
    else:
        print("File {} matched ".format(line))
        return 1

def writeToFile(line):
    f = open("file_to_upload.txt","a")
    f.write(line)

def readFile():
    with open("data.txt","r") as myfile:
        line = myfile.readline()
        while(line):
            flag = checkFileType(line)
            print(flag)
            if flag == 1:
                writeToFile(line)
            line = myfile.readline()

def mainFunction():
    readFile()

if __name__=='__main__':
    mainFunction()