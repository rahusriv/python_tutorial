fruits = []

while(True):
    fruit = input("Enter a fruit :")
    if(fruit == 'exit'):
        break

    fruits.append(fruit)

item = input("Which fruit you are looking for ? ")

if item in fruits :
    print(" Fruit is available")
else:
    print("Fruit is not available")


