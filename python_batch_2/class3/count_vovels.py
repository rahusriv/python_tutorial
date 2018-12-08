data = input("Please enter a sentence :")

count = 0
for char in data:
    if char in "aeiouAEIOU":
        count = count +1

print("There are {} vovels in the given sentence".format(count))