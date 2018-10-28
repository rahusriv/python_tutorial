
fruits = { "orange" : "A sweet and sour fruit",
           "apple": "good for health",
           "leamon": "has vitanin C in it ",
           "carrot": "Used as a salad",
           "mango": "Best summer fruit"}

#print(fruits.keys())

listofkeys = list(fruits.keys())
print(listofkeys)
listofkeys.sort()

for key in listofkeys:
    print("{}: {}".format(key,fruits[key]))
