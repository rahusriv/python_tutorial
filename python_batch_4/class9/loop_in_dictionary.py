fruit_dictionary = {"mango" : "King of fruits." , "pears": "Its a sour fruit"}

fruit_dictionary["orange"] = "Good in summers. Rich in Vitamin C"

fruit_dictionary["apple"] = "Fruit wich makes a pie or a jam"

for key in fruit_dictionary:
    print("Key : {} , Value : {} ".format(key,fruit_dictionary[key]))

for val in fruit_dictionary.values():
    print(val)

for key, val in fruit_dictionary.items():
    print(key)
    print(val)

