#Equality of lists

list1 = [2,4,6]

list2 = [6,4,2]

if list1 == sorted(list2) :
    print("Two lists are equal")
else:
    print("Lists are NOT equal")

#list3 = [2,4,6]
list3 = list1

if list1 is list3:
    print("Address space equal for both lists")
else:
    print("Address space NOT equal for both lists")

list3.append(8)
print(list1)