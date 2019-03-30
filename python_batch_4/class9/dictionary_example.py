fruit_dictionary = {"mango" : "King of fruits." , "pears": "Its a sour fruit"}

fruit_dictionary["orange"] = "Good in summers. Rich in Vitamin C"

fruit_dictionary["apple"] = "Fruit wich makes a pie or a jam"

print(fruit_dictionary)

fruit_name = input("Which fruit you like ? ")

#if fruit_name in fruit_dictionary:
#    fruit_desc = fruit_dictionary[fruit_name]
#    print("{} is {}".format(fruit_name,fruit_desc))
#else:
#    print("No fruit found")

fruit_desc = fruit_dictionary.get(fruit_name)

if fruit_desc != None:
    print("{} is {}".format(fruit_name,fruit_desc))
else:
    print("No fruit found")