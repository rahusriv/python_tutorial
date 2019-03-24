dish1= [1, "Chinese Noodles", ["egg", "noodles", "chilly", "mushroom"], 250.50, "m", "veg"]

dish2= [2, "Chicken Soup", ["chicken", "egg", "chilly", "vegetales"], 50.50, "s", "non-veg"]

dish3= [3, "Icecream Vanilla", ["milk", "sugar", "flavor"], 100.50, "d", "veg"]

dish4= [4, "Mix Veg Curry", ["carrot", "beans", "onions", "chilly"], 300.50, "m", "veg"]

dish5= [5, "Fried Babycorn", ["corn", "tomato", "chilly"], 220.50, "s", "veg"]

dish6= [6, "Tacos", ["corn", "chicken", "tomato", "chilly"], 120.50, "s", "non-veg"]

dish7= [7, "Dosa", ["rice", "tomato", "potato"], 80.50, "m", "veg"]

dish8= [8, "Dal Fry", ["toor", "butter", "chilly"], 130.50, "m", "veg"]

dish9= [9, "Nachos", ["cheese", "tomato", "potato"], 150.50, "s", "veg"]

dish10= [10, "Carrot Halwa", ["carrot", "ghee", "sugar"], 100.50, "d", "veg"]

dish11= [11, "Paneer Tikka", ["paneer", "tomato", "potato","chilly"], 170.50, "s", "veg"]

menu = [dish1, dish2, dish3, dish4, dish5, dish6, dish7, dish8, dish9, dish10, dish11]

print("***All Dishes with egg***")
count = 0
for dish in menu:
    ingridents = dish[2]
    if "egg" in ingridents:
        count = count + 1
        print("Option {} : Dish name is {}, Price is {}".format(count,dish[1],dish[3]))

print("***All Starters***")

count = 0
for dish in menu:
    if "s" == dish[4]:
        count = count + 1
        print("Option {} : Dish name is {}, Price is {}".format(count,dish[1],dish[3]))


print("Calculate bill :")

purchased_dishes = []
while(True):
    id = int(input("Enter id of the dish (Enter 0 to exit ): "))
    if id == 0:
        break
    else:
        purchased_dishes.append(id)

service_charge = int(input("Enter the service charge percentage: "))

total_bill = 0.0
for dish in menu:
    if dish[0] in purchased_dishes:
        total_bill = total_bill + dish[3]

print("Current bill = {}".format(total_bill))
service_charge_amount = (total_bill*service_charge)/100
print("Service Charge = {}".format(service_charge_amount))

print("Total Bill = {}".format(total_bill+service_charge_amount))
