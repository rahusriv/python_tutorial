fruits_list = ["apple", "mango", "banana", "orange"]

fruits_list.append("carrot")
fruits_list.insert(2,"new fruit")

print(type(fruits_list))

print(fruits_list)

#looping using for in loop
result = "Fruits in my basket are : "

for fruit in fruits_list:
    #print(fruit)
    result = result + fruit +" "

print(result)

#loop using index
for i in range(0,len(fruits_list)):
    print(fruits_list[i])