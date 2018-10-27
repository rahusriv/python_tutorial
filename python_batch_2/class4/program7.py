menu = []

dish1 = [1,"Egg Curry", 34.5,["egg", "onion","chilly"]]
dish2 = [2,"Pasta", 60.5,["egg", "noodles","cheese"]]
dish3 = [3,"Mashed Potato", 144.5,["potato", "onion","chilly"]]
dish4 = [4,"Salad", 55.5,["carrot", "radish","potato"]]
dish5 = [5,"Chapati", 66.5,["wheat", "salt"]]

menu.append(dish1)
menu.append(dish2)
menu.append(dish3)
menu.append(dish4)
menu.append(dish5)

item = input("Please tell me what you like ? ")

for dish in menu:
    if item in dish[3]:
        print(dish[1])

price = float(input("Tell us your budget ?"))

for dish in menu:
    if dish[2] < price:
        print(dish[1])
