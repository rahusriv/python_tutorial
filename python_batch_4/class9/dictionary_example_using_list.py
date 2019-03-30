fruit_list =[["mango" ,"King of fruits."], ["pears","Its a sour fruit"], ["orange","Good in summers. Rich in Vitamin C"],
             ["apple", "Fruit wich makes a pie or a jam"]]


fruit_name = input("Which fruit you like ? ")

for i in range(0,len(fruit_list)):
    fruit = fruit_list[i]
    if fruit_name in fruit:
        print("{} is {}".format(fruit_name,fruit[1]))
        break