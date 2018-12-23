shopping_list = []

shopping_list.append("TV")
shopping_list.append("Car")
shopping_list.append("Mobile")

print(shopping_list[0])
print(shopping_list[-1])

for item in shopping_list:
    print(item)

#shopping_list.sort()
print("#"*50)
sorted_shopping_list = sorted(shopping_list)

for item in sorted_shopping_list:
    print(item)

for i in range(0,len(shopping_list)):
    print(shopping_list[i])