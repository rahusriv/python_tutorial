
def addToList(l,item):
    l.append(item)

def deletFromList(l,item):
    l.remove(item)

def printList(l):
    for item in l:
        print(item)

def findElement(l,item):
    if item in l:
        print("Item found at index {} ".format(l.index(item)))
    else:
        print("Item not found")


shopping_list = []

while(True):
    print(" 1. Add ")
    print(" 2. Delete ")
    print(" 3. Print List")
    print(" 4. Find Item ")
    print("-1 to exit")

    choice = int(input("What you want to do ? "))

    if(choice == -1):
        break
    if(choice == 1):
        item = input("Enter item :")
        addToList(shopping_list,item)

    if(choice == 2):
        item = input("Enter item :")
        deletFromList(shopping_list,item)

    if(choice == 3):
        print("Shopping list is :")
        printList(shopping_list)

    if(choice == 4):
        item = input("Enter item :")
        findElement(shopping_list,item)

