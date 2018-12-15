fruits = { "orange" : "A sweet and sour fruit",
           "apple": "good for health",
           "leamon": "has vitanin C in it ",
           "carrot": "Used as a salad",
           "carrot": "Can be used in many side dishes",
           "mango": "Best summer fruit"}

key = input("Enter fruit you want to search: ")

#try catch
try:
    print(fruits[key])
except:
    print("Fruit not found")

#key in fruits
if key in fruits:
    print(fruits[key])
else:
    print("Fruit not found")

# get function
val = fruits.get(key)
if val != None:
    print(val)
else:
    print("Fruit not found")

#fruits["mango"] = "Seasonal fruit , very popular"

#print(fruits)

#Looping on a dictionary
for key in fruits:
    print("{} : {}".format(key,fruits[key]))

#Looping on values , not very efficient
for value in fruits.values():
    print(value)