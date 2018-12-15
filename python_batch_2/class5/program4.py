
def findKey(val):
    fruits = { "orange" : "A sweet and sour fruit",
               "apple": "good for health",
               "leamon": "has vitanin C in it ",
               "carrot": "Used as a salad",
               "mango": "Best summer fruit"}

    for key in fruits:
        if fruits[key] == val:
            return key


fruits = { "orange" : "A sweet and sour fruit",
           "apple": "Good for health",
           "leamon": "Gas vitanin C in it ",
           "carrot": "Used as a salad",
           "mango": "Best summer fruit"}

#print(fruits.keys())
#sorting based on key
listofkeys = list(fruits.keys())
print(listofkeys)
listofkeys.sort()

for key in listofkeys:
    print("{}: {}".format(key,fruits[key]))

#sorting based on value, create another list of list
listofvalues = list(fruits.values())
listofvalues.sort()
final_list = []
print(listofvalues)
for val in listofvalues:
    tmp = []
    key = findKey(val)
    tmp.append(key)
    tmp.append(val)
    final_list.append(tmp)
print(final_list)