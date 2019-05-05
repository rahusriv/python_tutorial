import re

def extractIP(line, res):
    line = line.strip()
    #print(line)
    p = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",re.IGNORECASE)
    ip_list = p.findall(line)
    #print(ip_list)
    res.extend(ip_list)

def readFile():
    res = []
    with open("ip_addr.txt","r") as myfile:
        line = myfile.readline()
        while(line):
            #print(line)
            extractIP(line, res)
            line = myfile.readline()
    print(res)

readFile()
