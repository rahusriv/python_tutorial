
def findFrequency(file_name):
    with open(file_name, "r") as myfile:
        para = myfile.read()
        words = para.split(" ")
        freq = {}
        for word in words:
            word1 = word.strip()
            if word1 in freq:
                val = freq[word1]
                val = val + 1
                freq[word1] = val
            else :
                freq[word1] = 1

    return freq

def findFrequencyPara(para):
    words = para.split(" ")
    freq = {}
    for word in words:
        word1 = word.strip()
        if word1 in freq:
            val = freq[word1]
            val = val + 1
            freq[word1] = val
        else :
            freq[word1] = 1
    return freq


def vectorMult(dict_user_para, dict_file):
    sum = 0
    for key in dict_user_para:
        if key in dict_file:
            sum = sum + (dict_user_para[key] * dict_file[key])
    return sum

def mainFunction():
    para = input("Enter something you want to search: ")
    user_dict = findFrequencyPara(para)
    d1 = findFrequency("file1.txt")
    d2 = findFrequency("file2.txt")
    d3 = findFrequency("file3.txt")

    score1 = vectorMult(user_dict,d1)
    score2 = vectorMult(user_dict,d2)
    score3 = vectorMult(user_dict,d3)

    print(d1)
    print(d2)
    print(d3)
    print(user_dict)

    print(score1)
    print(score2)
    print(score3)


mainFunction()