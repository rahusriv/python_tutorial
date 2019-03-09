para = input("Enter a sentence : ")

words = para.split(" ")

print(words)
#print("No of words is {} ".format(len(words)))
count = 0
for word in words:
    if len(word) == 0:
        pass
    else:
        print(word)
        count = count + 1

print("No of words is {} ".format(count))