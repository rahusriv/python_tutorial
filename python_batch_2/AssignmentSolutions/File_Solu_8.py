

def insertInDictionary(tmp, frequency):
    if tmp in frequency:
        val = frequency[tmp]
        val = val + 1
        frequency[tmp] = val
    else:
        frequency[tmp] = 1

myfile = open("/home/rahul/Desktop/sample.txt","r")
data = myfile.readlines()
print(data)

alllines = []
for line in data:
    tmp = line.strip()
    #tmp1 = line.strip("\n")
    alllines.append(tmp)

print(alllines)
frequency = {}
max = 0
max_word = ""
count = 0

for line in alllines:
    mylist = line.split(" ")
    for word in mylist:
        count = count +1
        tmp = word.strip()
        insertInDictionary(tmp,frequency)
        size = len(tmp)
        if size > max:
            max = size
            max_word = tmp

print("No of words = {}".format(count))
print("Longest word is {}, of length {}".format(max_word,max))
print(frequency)