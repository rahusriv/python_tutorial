pattern = input("Please enter a pattern : ")
num = int(input("Please enter a number :"))

extracted_number = int(pattern[0::2])

res = extracted_number * num

print(res)
