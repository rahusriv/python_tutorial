mylist = []

for i in range(0,6):
    name = input("Enter a name :")
    mylist.append(name)

print(mylist)

#mylist.sort()  # It works on the same list
new_list = sorted(mylist) #It creates a new list and sorts that list, Original list remains intact

print(new_list)
