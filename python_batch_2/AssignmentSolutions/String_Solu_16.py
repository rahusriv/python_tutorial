data = input("Enter a string :")

value = input("Enter a value: ")

middle = int(len(data)/2)
result = data[0:middle] + value + data[middle:]

print(result)