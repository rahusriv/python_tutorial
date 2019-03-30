para = input("Enter commas seperated words:")

word_list = para.split(",")

frequency_dict = {}

for word in word_list:
    if word in frequency_dict:
        val = frequency_dict[word]
        val = val +1
        frequency_dict[word] = val
    else:
        frequency_dict[word] = 1

print(frequency_dict)

print(frequency_dict["mango"])

max = -1
max_fruit = ""

for key in frequency_dict:
    if frequency_dict[key] > max:
        max = frequency_dict[key]
        max_fruit = key

print(max_fruit)
print(max)