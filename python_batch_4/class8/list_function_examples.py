fruits_list = ["apple", "mango", "banana", "orange", "mango", "mango", "papaya"]

fruits_list.insert(1,"kiwi")
fruits_list.append("guava")
print(fruits_list)
fruits_list.extend(["grapes","butter fruiy","peach"])

print(fruits_list)

ind = fruits_list.index("mango")
print("Index of mango is : {}".format(ind))

fruits_list.remove("mango")

print(fruits_list)

last_element = fruits_list.pop()
print("LAst element of the list is : {}".format(last_element))

print(fruits_list)

fruits_list.reverse()
print(fruits_list)

fruits_list.sort()
print(fruits_list)

fruits_list_copy = fruits_list.copy()
print(fruits_list_copy)

