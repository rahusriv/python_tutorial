fruits = { "orange" : "A sweet and sour fruit",
           "apple": "good for health",
           "leamon": "has vitanin C in it ",
           "carrot": "Used as a salad",
           "mango": "Best summer fruit"}

name = input("What fruit you like ?")

#print(fruits[name])

#print(fruits.get(name))

if name in fruits:
    print(fruits[name])
else:
    print("Fruit not found")

if fruits.get(name)!=None:
    print(fruits.get(name))
    print(fruits[name])
else:
    print("Again fruit not found")


