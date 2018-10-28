#Looping in a dictionary

#Looping using keys

fruits = { "orange" : "A sweet and sour fruit",
           "apple": "good for health",
           "leamon": "has vitanin C in it ",
           "carrot": "Used as a salad",
           "mango": "Best summer fruit"}

for key in fruits:
    print("{}: {}".format(key,fruits[key]))

print("#"*50)

for val in fruits.values():
    print(val)

for key,val in fruits.items():
    print(key)
    print(val)